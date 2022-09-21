import FileReader
import requests
from bs4 import BeautifulSoup
import re

Separator = "%20"


class Scraper:

    def __init__(self):
        pass


def link(uri, label=None):
    if label is None:
        label = uri
    parameters = ''

    # OSC 8 ; params ; URI ST <name> OSC 8 ;; ST
    escape_mask = '\033]8;{};{}\033\\{}\033]8;;\033\\'

    return escape_mask.format(parameters, uri, label)


def Start(cousine: str, keywords: list):
    conf = FileReader.LoadConfiguration()

    websites = FileReader.GetWebSitesList()
    for url in websites:
        print("sending request to " + url)
        searchRequest = url + f"/search/results/?search={cousine}"
        for kw in keywords:
            searchRequest += Separator + kw
        httpResponse = requests.get(searchRequest)
        print(httpResponse.status_code)
        soup = BeautifulSoup(httpResponse.text, 'html.parser')
        divs = soup.find_all(
            'div', {'class': re.compile('.*detailsContainer(?=.*[aA-zZ])')})
        for i in range(conf["MaxResNumDisplayed"]):
            if i == len(divs):
              break
            tag = divs[i].find('a')
            if tag is None:
              continue
            print(f"{i+1}: "+ tag.get('title') + "-->" + tag.get('href')+"\n")

