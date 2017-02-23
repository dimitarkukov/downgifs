#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import sys


print(len(sys.argv))

if len(sys.argv) < 3:  # checks for enough arguments
    print("Usage: getAllTheGifs.py 'number of pages' 'path to save'")
    exit()  # exits without executing code below


filenames = []
urls = []


def get_gifs():
    page = 1
    while page <= int(sys.argv[1]):
        url_of_page = "http://thecodinglove.com/page/" + str(page)
        source_code = requests.get(url_of_page)
        plain_source_code = source_code.text  # no header source
        soupobj = BeautifulSoup(plain_source_code) # make a bs object
        for link in soupobj.findAll("img"):  # find all images
            if link["src"].lower().endswith("gif"):  # find all gifs
                urls.append(link["src"])  # add link to urls lists
        page += 1


def get_titles():
    page = 1
    while page <= int(sys.argv[1]):
        url_of_page = "http://thecodinglove.com/page/" + str(page)
        source_code = requests.get(url_of_page)
        plain_source_code = source_code.text  # no header source
        soupobj = BeautifulSoup(plain_source_code)
        for link in soupobj.findAll('div', attrs={'class': 'post'}):  # find divs with class type post
            filename = link.find('a').contents[0]  # this gets the text in an a href tag
            filenames.append(filename)  # append text to filenames list
        page += 1


def save_to_pc():
    dict_from_lists = dict(zip(filenames, urls))  # makes a key values pair from the two lists
    os.mkdir(sys.argv[2])
    for f, u in dict_from_lists.items():
        fullpath = os.path.join(sys.argv[2], f)  # fullpath with filename
        urllib.request.urlretrieve(u, fullpath)  # download using url and fullpath


if __name__ == '__main__':
    get_gifs()  # set the number of pages to crawl
    get_titles()  # set the number of pages to crawl
    save_to_pc()
