import PySimpleGUI as uiHandler
import FileReader
import webbrowser

ss_image = './img/splash_screen.png'
ss_display_time_ms = 4000
def_width = 600
def_height = 600

class GuiBuilder:

    def __init__(self):
        pass

def ShowSplashScreen():
  uiHandler.theme("DarkTeal 6")
  uiHandler.Window("MakeEatEasy", [[uiHandler.Image(ss_image)]], size = (def_width,def_height)).read(timeout=ss_display_time_ms, close=True)

def BuildMainWindow() -> dict:
  conf = FileReader.LoadConfiguration()
  cuisines = conf["cuisines"]
  ingredients = conf["ingredients"]

  layout=[ [uiHandler.Text("What would you like to eat?", font='lucida', justification='left') ],
           [uiHandler.Listbox(values=cuisines, size=(50,3), select_mode="single", key="-CUISINE-") ],
           [uiHandler.Text("What do you have in your fridge?", font='lucida', justification='left') ],
           [uiHandler.Listbox(values=ingredients, size=(50,3), select_mode="multiple", key="-INGREDIENTS-") ],
           [uiHandler.Button("search"), uiHandler.Exit() ] ]

  window = uiHandler.Window("MakeEatEasy", layout, size = (def_width,def_height), resizable=True, finalize=True )

  event, values = window.read()
  if event=="search" or event == uiHandler.WIN_CLOSED:
    window.close()
    return values

def BuildDisplayWindow( urls ):
  font = ('Courier New', 10)
  col = [[uiHandler.Text(urls[idx], tooltip=urls[idx], enable_events=True, font=font,
    key=f'URL {urls[idx]}')] for idx in range(len(urls))]
  layout = [
    [uiHandler.Column(col, scrollable=True, key = "Column", expand_x=True, expand_y=True)],
    [uiHandler.Exit(), uiHandler.Button('Up', key = "up"), uiHandler.Button('Down', key = "down")],
]
  window = uiHandler.Window('Results', layout, resizable=True, finalize=True, size = (def_width,def_height))

  firstLink = True
  while True:
    event, values = window.read()
    print(event)
    if event == uiHandler.WINDOW_CLOSED or event=="Exit":
        break
    elif event == "down":
        window['Column'].Widget.canvas.yview_moveto(1.0)
    elif event == "up":
        window['Column'].Widget.canvas.yview_moveto(0.0)
    elif event.startswith("URL "):
        url = event.split(' ')[2].strip()
        print(url)
        if firstLink:
          webbrowser.open_new(url)
          firstLink = False
        else:
          webbrowser.open_new_tab(url)

  window.close()
  
  