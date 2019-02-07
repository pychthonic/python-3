import sys
import re

import requests


class InstagramList:
    """Opens a text file containing a list of celebrity names (one name
    per line), then uses Bing to find their public instagram profile
    links, puts the links in a list, and provides a function to print
    the links out.
    """
    def __init__(self, filename):
        # Creates list of names found in filename text file
        self.filename = filename
        self.bing_search_link_list = []
        self.ig_link_list = []
        with open(self.filename, "r") as fd:
            self.names = fd.readlines()

    def get_bing_search_link_list(self):
        """Uses list of names from __init__ to create a list of Bing
        search URLs.
        """
        for name in self.names:
            name = name.strip().replace(" ", "+")
            search_term = name + "+instagram"
            bing_search_link = (
                'https://www.bing.com''/search?q={}&ia=web'
                ).format(search_term)
            self.bing_search_link_list.append(bing_search_link)

    def bing_search(self):
        """Sends HTTP request packets to the list of bing search URLs
        from get_bing_search_link_list() and uses regular expressions to
        parse the response packets for the public Instagram link.
        Creates list of these links called ig_link_list.
        """
        if not self.bing_search_link_list:
            print("Error: no Bing URLs found.")
            sys.exit()

        ua = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)'
            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116'
            ' Safari/537.36'
            }

        for bing_search_link in self.bing_search_link_list:
            response = requests.get(bing_search_link, headers=ua)
            try:
                found = re.search('rch Results(.+?)</', response.text).group(1)
                ig_link = re.search('a href="(.+?)"', found).group(1)
            except AttributeError as err:
                ig_link = "link not found"
            self.ig_link_list.append(ig_link)

    def print_instagram_links(self):
        """Prints out the list of Instagram links."""
        for ig_link in self.ig_link_list:
            print(ig_link)


if __name__ == '__main__':
    ig_list = InstagramList("instagram_name_list.txt")
    ig_list.get_bing_search_link_list()
    ig_list.bing_search()
    ig_list.print_instagram_links()
