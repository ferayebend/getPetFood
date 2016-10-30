import os, sys
import requests
from lxml import etree


def findPetFoodURLs(top_url):
    urls = []
    return urls

def getHtml(url):
    req = requests.get(url)
    # add retry instances
    return req.content

def getCalorie(html_string):
    calorie = ''
    return calorie

def main():
    pass

if __name__ == '__main__':
    main()
