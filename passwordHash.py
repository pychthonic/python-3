from hashlib import sha256
from getpass import getpass
import re


class loginSession:

    """This program demonstrates the principles behind password hashing, that is, 
    how computers authenticate users. Instead of keeping databases full of 
    passwords, which would be an obvious target for roving botnets, they often store 
    hashes of the passwords. When a user enters their password, the computer makes 
    a hash of that password and compares it to its stored hash for the user. If the 
    two hashes match, the user is authenticated. A hash is an irreversible 
    algorithm - it takes a string of characters (the password), and scrambles it 
    into a long string of what look like random characters called the hash. You 
    can always get the hash if you have the password (you can use sha256 to 
    make a hash of the password 'password1234' on a tuesday then run sha256 on 
    'password1234' a year later on a different computer in a different country and 
    you'll get the same hash), but you can't go in the opposite direction and get 
    the password from the hash, except with an unsafe hash algorithm like sha1 or
    MD5, neither of which should be used to protect sensitive information. The 
    sha256 hashing algorithm is chugging along just fine, and is safe to use (as
    of 2018...).
    
    The program asks the user to either login with an existing username or create 
    a username and password. The first time the program is run, it creates an 
    archive file kept in the same directory the executable was run from, called 
    'hashes.archive'. That file contains hashes of the usernames and passwords that 
    are created through the program, so someone who opens the file can only see how 
    many people have created accounts, and nothing more.
   
    It uses regular expressions to make sure the created usernames are letters, 
    numbers, and underscores, and that passwords contain at least one lowercase 
    letter, one uppercase letter, one number, and one of these symbols: !@#$%^&*()
    
    One goal to work on for this project is to import the os module and give an admin
    user some options, such as changing the permission bits of the hash archive, or 
    encrypting the archive, or hashing the archive between login sessions to give 
    the archive file more integrity, that is to say, give the user a small bit more 
    certainty that the archive file is the same one it's sposed to be, basically 
    toying with ways to make it more secure, knowing of course that it's a toy.

    """

    def __init__(self):
        
        self.loginName = input("Login Name (Press Enter to create new user): ")
        
        self.success = False            #lol @ self.success = False

        if not self.loginName:
            self.loginName = input("\nEnter new login name: ")

            while not self.isValidLogin(self.loginName):
                self.loginName = input("\nEnter new login name: ")

            self.loginHash = sha256(self.loginName.encode()).hexdigest()
    
            self.pwString = ""

            while not self.isValidPassword(self.pwString):
                print("\nPassword must be 8 or more characters and contain at least "
                        "one of each of the following: \n\t -uppercase letters \n\t "
                        "-lowercase letters \n\t -numbers \n\t -one of more of these "
                        "symbols: !@#$%^&*()\n")
                self.pwString = getpass("Enter new password: ")

            self.passwordHash = sha256(self.pwString.encode()).hexdigest()
    
            with open('hashes.archive', 'a') as self.passwordFile:
                self.passwordFile.write('login hash: {} : password hash: {}\n'.format(
                    self.loginHash, self.passwordHash))

        try:
            with open('hashes.archive', 'r') as self.passwordFile:
    
                self.Found = False

                for self.line in self.passwordFile:
                    self.loginEntryLine = self.line.split(':')
                    if self.loginEntryLine[1].strip() == sha256(self.loginName.encode()).hexdigest():
                        print("Hello {}".format(self.loginName))
                        self.Found = True
                        break
     
                if not self.Found:
                    print("Login name not found.")

                if self.Found:
        
                    self.passwordTries = 0
                    while self.passwordTries < 3:
                        if sha256(getpass("Enter your password: ").encode()).hexdigest() == \
                        self.loginEntryLine[3].strip():
                            print("Congrats, you remembered your password.\n")
                            self.success = True
                            break
                        else:
                            self.passwordTries += 1
                            print("Wrong password. {} more tries\n".format(3 - self.passwordTries))

        except FileNotFoundError:
    
            print("\nNo hashes.archive file was found because you haven't made your first account yet. "
            "When that happens, a file will be created called hashes.archive to store username & "
            "password hashes (not the usernames and passwords themselves).\n")

    def isValidLogin(self, loginString):
        if re.match('^[a-zA-Z0-9_]+$', loginString):
            return True
        else:
            print("\nLogin names must be only letters, numbers, or _\n")

    def isValidPassword(self, pwString):
        if (8 <= len(pwString) < 256) and re.match('^[a-zA-Z0-9!@#$%^&*()]+$', pwString) and \
        re.search('[a-z]', pwString) and re.search('[A-Z]', pwString) and re.search('[0-9]', \
                pwString) and re.search('[!@#$%^&*()]', pwString):
            return True
        else:
            return False
    
    def successfulLogin(self):
        return self.success

if __name__ == '__main__':
    sesh = loginSession()
