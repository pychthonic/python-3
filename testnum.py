import requests, ordinalize

"""
I wrote this program to check the accuracy of ordinalize.py, also found in this repository.
It uses requests to go to http://www.isthe.com/cgi-bin/chongo/number.cgi and submit the
number input by the user to the form there. It then downloads the HTTP response, parses it
for and removes the number, ordinalizes the number (five -> fifth, etc) and then uses
ordinalize.py as a module to get what should be the same number. It lastly removes 
punctuation, checks whether the two strings are equal, and lets the user know either way.

For now it will be used to check my progress toward infinity but when I hammer out the kinks
in ordinalize.py I'll do the same for this guy.


"""

num = input("Enter a number: ")

data = {"number": num}

numFromOrdinalize = ordinalize.getordnum(num).replace('-', ' ')

print("\nNumber from ordinalize.py: \n" + numFromOrdinalize + '\n')


#################

r = requests.post("http://www.isthe.com/cgi-bin/chongo/number.cgi", data=data);

body_data = r.text

beforeNumStr = "<PRE>"
afterNumStr = "</PRE>"

result = body_data[body_data.find(beforeNumStr)+ len(beforeNumStr):body_data.rfind(afterNumStr)].strip().split()

result = ' '.join(result).replace(',', '')

numFromWeb = ordinalize.makeOrdinal(result)

print("\nUsing Requests to consult the web, we get:\n" + numFromWeb + '\n')


################

if numFromOrdinalize == numFromWeb:
    print("\nWe have a match on our hands people!!\n")
else:
    print("\nSomethings at least a little off...\n")






