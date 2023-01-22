import FileReader
import requests
from bs4 import BeautifulSoup
import re
#TODO main is also handling the gui builder, it should be changed
import GuiBuilder

Separator = "%20"
#TODO consider hashing websites as key
lookUp = {
  'https://www.halfbakedharvest.com/': 'post-summary_.*',
  'https://www.allrecipes.com/': '.*card-list.*',
  'https://tasty.co/': '.*feed__.*'
}

search = {
  'https://www.halfbakedharvest.com/': '/?s=',
  'https://www.allrecipes.com/': '/search?q=',
  'https://tasty.co/': 'search?q='
}

separators = {
  'https://www.halfbakedharvest.com/': '+',
  'https://www.allrecipes.com/': '%20',
  'https://tasty.co/': '%20'
}


class Scraper:

  def __init__(self):
    pass


def Start(cuisine: str, keywords: list):
  res = []
  conf = FileReader.LoadConfiguration()

  websites = FileReader.GetWebSitesList()
  for url in websites:
    print("sending request to " + url)
    res.append("Results from " + url)
    searchRequest = url + search[url] + cuisine
    for kw in keywords:
      searchRequest += separators[url] + kw
    httpResponse = requests.get(searchRequest)
    print(httpResponse.status_code)
    soup = BeautifulSoup(httpResponse.text, 'html.parser')
    divs = soup.find_all('div', {'class': re.compile(lookUp[url])})
    displayedResults = 0
    for d in divs:
      tags = d.find_all('a')
      #if tags is None:
      #   continue
      for t in tags:
        displayedResults += 1
        if displayedResults > conf["MaxResNumDisplayed"]:
          break
        res.append(CreateResultRow(displayedResults, t, url))


#TODO
#1: consider gettig input for rating and insert rate in dictionary. this should be sorted and display only the first x elements
#2: filter by complexity
  GuiBuilder.BuildDisplayWindow(res)


def CreateResultRow(idx: int, tag: object, baseUrl: str) -> str:
  
  output = f"{idx}: "
  if tag.get('title'):
    link = tag.get('title')
    output += link + "-->"
  if tag.get('href'):
    link = tag.get('href')
    #Some website have only partial hyperlinks
    if not link.startswith('https'):
      link = baseUrl + link
    output += link + "\n"
  
  return output
