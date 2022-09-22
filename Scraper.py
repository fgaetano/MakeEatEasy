import FileReader
import requests
from bs4 import BeautifulSoup
import re

Separator = "%20"
#TODO consider hashing websites as key
lookUp = {
  'https://www.halfbakedharvest.com/': 'post-summary_.*', 
  'https://www.allrecipes.com/': '.*detailsContainer(?=.*[aA-zZ])'
}

search = {
  'https://www.halfbakedharvest.com/': '/?s=', 
  'https://www.allrecipes.com/': '/search/results/?search='
}

separators = {
  'https://www.halfbakedharvest.com/': '+', 
  'https://www.allrecipes.com/': '%20'
}

class Scraper:

    def __init__(self):
        pass

def Start(cousine: str, keywords: list):
    conf = FileReader.LoadConfiguration()

    websites = FileReader.GetWebSitesList()
    for url in websites:
        print("sending request to " + url)
        searchRequest = url + search[url] + cousine
        for kw in keywords:
            searchRequest += separators[url] + kw
        httpResponse = requests.get(searchRequest)
        print(httpResponse.status_code)
        soup = BeautifulSoup(httpResponse.text, 'html.parser')
        divs = soup.find_all(
            'div', {'class': re.compile(lookUp[url])})
        for i in range(conf["MaxResNumDisplayed"]):
            if i == len(divs):
              break
            tag = divs[i].find('a')
            if tag is None:
              continue
            PrintOutResult( i+1, tag )
          
#TODO 
          #1: consider gettig input for rating and insert rate in dictionary. this should be sorted and display only the first x elements
          #2: filter by complexity


def PrintOutResult( idx:int, tag:object ):
  output = f"{idx}: "
  if tag.get('title'):
    output += tag.get('title') + "-->"
  if tag.get('href'):
    output += tag.get('href')+"\n"
  print(output)