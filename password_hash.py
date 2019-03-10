from hashlib import sha256
from getpass import getpass
import re


class LoginSession:
    """This program demonstrates password hashing, that is, how
    computers authenticate users. Instead of keeping databases full of
    plaintext passwords, or even encrypted passwords, they often store
    hashes of the passwords. When a user enters their password, the
    computer makes a hash of that password and compares it to its stored
    hash for the user. If the two hashes match, the user is
    authenticated. A hash cipher is an irreversible algorithm - it takes
    a string of characters (in this case, the password), and scrambles
    it into a long string of what look like random characters called the
    hash. You can always get the hash if you have the password (you can
    use sha256 to make a hash of the password 'password1234' on a
    Tuesday then run sha256 on 'password1234' a year later on a
    different computer in a different country and you'll get the same
    hash), but you can't go in the opposite direction and get the
    password from the hash, except with an unsafe hash algorithm like
    sha1 or MD5, neither of which should be used to protect sensitive
    information. The sha256 hashing algorithm is chugging along just
    fine, and is safe to use (as of 2018...).

    The program asks the user to either login with an existing username
    or create a username and password. The first time the program is
    run, it creates an archive file kept in the same directory the
    executable was run from, called 'hashes.archive'. That file contains
    hashes of the usernames and passwords that are created through the
    program, so someone who opens the file can only see how many people
    have created accounts, and nothing more.

    It uses regular expressions to make sure the created usernames are
    letters, numbers, and underscores, and that passwords contain at
    least one lowercase letter, one uppercase letter, one number, and
    one of these symbols: !@#$%^&*()
    """
    def __init__(self):
        """Prompt user for username. If user chooses to make a new
        username, 1/ allow user to input new username, 2/ check
        whether new username is valid, 3/ create hash of username,
        4/ accept password and check its validity, 5/ create hash of
        password, 6/ write hash to hashes.archive file. If user
        wishes to login using an existing username/password, hash
        the username input by the user, and check it with each line 
        in the hashes.archive file. If it is not found, "user not 
        found" is output to the screen. If the username hash is found,
        the boolean "found" variable is toggled to True, and the user is
        given three chances to enter the correct password. Each password
        is hashed and compared to the hash found next to the hash of
        the login name in the hashes.archive file.
        """
        self.login_name = input(
            "Login Name (Press Enter to create new user): ")
        self.login_success = False

        if not self.login_name:
            self.login_name = input("\nEnter new login name: ")
            while not self.is_valid_login(self.login_name):
                self.login_name = input("\nEnter new login name: ")
            self.login_hash = sha256(self.login_name.encode()).hexdigest()
            self.pw_string = ""

            while not self.is_valid_password(self.pw_string):
                print("\nPassword must be 8 or more characters and contain at "
                      "least one of each of the following: \n\t -uppercase "
                      "letters \n\t -lowercase letters \n\t -numbers \n\t -one"
                      " or more of these symbols: !@#$%^&*()\n")
                self.pw_string = getpass("Enter new password: ")

            self.password_hash = sha256(self.pw_string.encode()).hexdigest()

            with open('hashes.archive', 'a') as self.password_file:
                self.password_file.write(
                    f"login hash: {self.login_hash} : "
                    f"password hash: {self.password_hash}\n")

        try:
            with open('hashes.archive', 'r') as self.password_file:
                self.found = False

                for line in self.password_file:
                    login_entry_line = line.split(':')
                    if login_entry_line[1].strip() == sha256(
                            self.login_name.encode()).hexdigest():
                        print("Hello {}".format(self.login_name))
                        self.found = True
                        break

                if not self.found:
                    print("Login name not found.")

                if self.found:
                    self.password_tries = 0
                    while self.password_tries < 3:
                        if (sha256(getpass(
                                "Enter your password: "
                                ).encode())).hexdigest() == \
                                login_entry_line[3].strip():
                            print("Congrats, you remembered your password.\n")
                            self.login_success = True
                            break
                        else:
                            self.password_tries += 1
                            print(f"Wrong password. {3 - self.password_tries}"
                                  " more tries\n")
        except FileNotFoundError as err:
            print("\nNo hashes.archive file was found because you haven't "
                  "made your first account yet. When that happens, a file "
                  "will be created called hashes.archive to store username & "
                  "password hashes (not the usernames and passwords "
                  "themselves).\n")

    def is_valid_login(self, login_string):
        """Use regular expressions to check the validity of a new
        username.
        """
        if re.match('^[a-zA-Z0-9_]+$', login_string):
            return True
        else:
            print("\nLogin names must be only letters, numbers, or _\n")
            return False

    def is_valid_password(self, pw_string):
        """Use regular expressions to check validity of new password."""
        if (8 <= len(pw_string) < 256) and re.match(
                '^[a-zA-Z0-9!@#$%^&*()]+$', pw_string) and re.search(
                '[a-z]', pw_string) and re.search(
                '[A-Z]', pw_string) and re.search(
                '[0-9]', pw_string) and re.search(
                '[!@#$%^&*()]', pw_string):
            return True
        else:
            return False

    def successful_login(self):
        """Return True or False depending on whether login was
        successful.
        """
        return self.login_success


if __name__ == '__main__':
    sesh = LoginSession()
