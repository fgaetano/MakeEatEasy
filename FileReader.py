import json

filename = "WebSites.txt"
#TODO:Move conf reader elsewhere
config_file = "conf.json"


class InputValidator:

    def __init__(self):
        pass


def GetWebSitesList() -> list:
    file = open(filename, 'r')
    sites = file.readlines()
    file.close()
    return sites


def LoadConfiguration() -> dict:
    conf = open(config_file, 'r')
    conf_dict = json.load(conf)
    conf.close()
    return conf_dict
