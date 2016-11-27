import re
import sys
import urllib
import io
import urlparse
import json
import csv
from BeautifulSoup import BeautifulSoup
import nltk
from urllib import urlopen
from bs4 import BeautifulSoup


class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


data = {}
def gett():
    url = "http://www.50states.com/facts/alabama.htm"
    html = urlopen(url).read()
    raw = nltk.clean_html(html)
    print(raw)



def get():
    link = "http://www.50states.com/facts/alabama.htm"
    f = urllib.urlopen(link)
    myfile = f.read()
    print myfile


#target = io.open("output.txt", "w+", encoding="latin1")

def process(url):
    myopener = MyOpener()
    # page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    for tag in soup.findAll('li', href=True):
        tag['li'] = urlparse.urljoin(url, tag['li'])
        print tag['li']
#filename = 'output.txt'


def gettt():
    #url = "http://www.50states.com/facts/alabama.htm"
    with open('statesDB.txt', 'rU') as f:
        for line in f:
            curr_state_list = []
            html = urllib.urlopen(line).read().strip()
            soup = BeautifulSoup(html, "html.parser")


            state = line[30:]
            # state = state.strip()
            state.replace(" ", "")
            state_name = state[:-5]
            for link in soup.ol:
                ab = str(link)[11:]
                bc = ab[:-5]
                cd = bc.strip("\n").strip(" ")
                curr_state_list.append(cd)
                #print(cd)
            data[state_name] = curr_state_list

        return data
dict = gettt()
json.dump(dict, open("output.txt",'w'))
