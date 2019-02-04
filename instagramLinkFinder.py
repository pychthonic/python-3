import requests, re, sys


class InstagramList:

    """

    Opens a text file containing a list of celebrity names (one name per line), 
    then uses Bing to find their public instagram profile links, puts the links 
    in a list, and provides a function to print the links out.

    """

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
