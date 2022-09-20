import FileReader
import requests
from bs4 import BeautifulSoup
import re


class InputValidator:

    def __init__(self):
        pass


def Start(cousine: str):
    conf = FileReader.LoadConfiguration()
  
    websites = FileReader.GetWebSitesList()
    for url in websites:
        print("sending request to " + url)
        searchRequest = url + f"/search/results/?search={cousine}"
        httpResponse = requests.get(searchRequest)
        print(httpResponse.status_code)
        soup = BeautifulSoup(httpResponse.text, 'html.parser')
        tags = soup.find_all('a', {'class': re.compile('.*card__titleLink.*')})
        for i in range(conf["MaxResNumDisplayed"]):
            print(tags[i].get('title'))
