filename = "WebSites.txt"

class InputValidator:
  def __init__(self):
        pass
    
def GetWebSitesList() -> list:
  file =  open(filename, 'r')
  sites = file.readlines()
  return sites