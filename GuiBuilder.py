import PySimpleGUI as uiHandler
import FileReader

ss_image = './img/splash_screen.png'
ss_display_time_ms = 4000

class GuiBuilder:

    def __init__(self):
        pass

def ShowSplashScreen():
  uiHandler.Window("WuhToEat",[[uiHandler.Image(ss_image)]]).read(timeout=ss_display_time_ms, close=True)

def BuildMainWindow() -> dict:
  conf = FileReader.LoadConfiguration()
  cousines = conf["cousines"]
  ingredients = conf["ingredients"]

  layout=[ [uiHandler.Text("What would you like to eat?", font='lucida', justification='left') ],
           [uiHandler.Listbox(values=cousines, size=(30,3), select_mode="single", key="-COUSINE-") ],
           [uiHandler.Text("What do you have in your fridge?", font='lucida', justification='left') ],
           [uiHandler.Listbox(values=ingredients, size=(30,3), select_mode="multiple", key="-INGREDIENTS-") ],
           [uiHandler.Button("search"), uiHandler.Exit() ] ]

  window = uiHandler.Window("WuhToEat", layout )
  event, values = window.read()
  #if event( uiHandler.WIN_CLOSED, 'EXIT' ):
    #return 
  if event=="search" or event == uiHandler.WIN_CLOSED:
    window.close()
    return values

def BuildDisplayWindow( links ):
  #Todo: see https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field to crate links to website
  layout = [[uiHandler.Listbox(values = links, size=(80,40))],
           [uiHandler.Button("Close")]]
  window = uiHandler.Window("Results", layout)
  event = window.read()
  if event == "Close" or event == uiHandler.WIN_CLOSED:
    return
  
  