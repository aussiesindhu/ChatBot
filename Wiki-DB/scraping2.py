import re
import sys
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup
import re

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


def process(url):
    myopener = MyOpener()
    # page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    pattern = re.compile("http://www.50states.com/facts/")

    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if(pattern.match(tag['href'])):
            print tag['href']

process("http://www.50states.com/facts/")
