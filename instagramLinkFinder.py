import requests, re

"""
I wrote this script as a response to a stackoverflow question and decided to post it here since 
it's kinda nifty. It opens up a file with a list of celebrity names (found in this repository as 
"instagramNameSearchList.txt" and uses the requests module and Bing to search for their public 
instagram accounts. It then uses regular expressions to parse the returned packet for the link 
and prints it to the screen.

"""


def bingsearch(searchfor):                                                                                                                                                                                       
    link = 'https://www.bing.com/search?q={}&ia=web'.format(searchfor)                                                                                                                            
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}

    payload = {'q': searchfor}                                                                                                                                                                                 
    response = requests.get(link, headers=ua, params=payload)               

    try:
        found = re.search('Search Results(.+?)</a>', response.text).group(1)
        iglink = re.search('a href="(.+?)"', found).group(1)
    except AttributeError:
        iglink = "link not found"

    return iglink


with open("instagramNameSearchList.txt", "r") as f:
    names = f.readlines()

for name in names:
    name = name.strip().replace(" ", "+")
    searchterm = name + "+instagram"

    IGLink = bingsearch(searchterm)

    print(IGLink)




