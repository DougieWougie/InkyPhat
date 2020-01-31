from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


# Function accesses the URL, creates a BS object and parses it for the two LI elements.
# The first of these is the next due collection type and date. Function takes the integer
# from the end of the URL on the site.
def bin_day(locator):
    url = 'https://bmsdchosting.net/waste-services/mid-suffolk-bin-collection/weeks/' + str(locator)
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        li_list = bs.findAll('li')
    except HTTPError as e:
        return e
    except URLError as e:
        return 'Server not available'
    return li_list[0].get_text()


print(bin_day(47159))
