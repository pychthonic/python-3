import requests, re, sys

"""
I wrote this script as a response to a stackoverflow question and 
decided to post it here since it's kinda nifty. It opens up a file with 
a list of celebrity names (found in this repository as 
"instagramNameSearchList.txt" and uses the requests module and Bing to 
search for their public instagram accounts. It then uses regular 
expressions to parse the returned packet for the link and prints it to 
the screen.

"""

class InstagramList:

    bingSearchLinkList = []
    igLinkList = []

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, "r") as self.fd:
            self.names = self.fd.readlines()

    def getBingSearchLinkList(self):
        for name in self.names:
            name = name.strip().replace(" ", "+")
            searchTerm = name + "+instagram"
            bingSearchLink = ('https://www.bing.com'
                '/search?q={}&ia=web').format(searchTerm)
            self.bingSearchLinkList.append(bingSearchLink)

    def bingSearch(self):
        if not self.bingSearchLinkList:
            print("Error: no Bing URLs found.")
            sys.exit()

        ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116'
        ' Safari/537.36'}

        for bingSearchLink in self.bingSearchLinkList:
            response = requests.get(bingSearchLink, headers=ua)
            try:
                found = re.search('Search Results(.+?)</a>', 
                    response.text).group(1)
                igLink = re.search('a href="(.+?)"', found).group(1)
            except AttributeError as err:
                igLink = "link not found"
            self.igLinkList.append(igLink)

    def printInstagramLinks(self):
        for igLink in self.igLinkList:
            print(igLink)


if __name__ == '__main__':
    igList = InstagramList("instagramNameSearchList.txt")
    igList.getBingSearchLinkList()
    igList.bingSearch()
    igList.printInstagramLinks()
