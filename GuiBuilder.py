import PySimpleGUI as uiHandler
import FileReader
import webbrowser

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
  if event=="search" or event == uiHandler.WIN_CLOSED:
    window.close()
    return values

def BuildDisplayWindow( urls ):
  font = ('Courier New', 16, 'underline')
  layout = [[uiHandler.Text(urls[idx], tooltip=urls[idx], enable_events=True, font=font,
    key=f'URL {urls[idx]}')] for idx in range(len(urls))]
  window = uiHandler.Window('Results', layout, finalize=True)

  firstLink = True
  while True:
    event, values = window.read()
    print(event)
    if event == uiHandler.WINDOW_CLOSED:
        break
    elif event.startswith("URL "):
        url = event.split(' ')[2].strip()
        print(url)
        if firstLink:
          webbrowser.open_new(url)
          firstLink = False
        else:
          webbrowser.open_new_tab(url)

  window.close()
  
  