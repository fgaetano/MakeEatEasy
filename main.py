import Scraper
import GuiBuilder


def main():
    GuiBuilder.ShowSplashScreen()
    params = GuiBuilder.BuildMainWindow()
    if params is not None:
      foodType = params["-CUISINE-"][0]
      kws = params["-INGREDIENTS-"]
      Scraper.Start(foodType, kws)
    return;

if __name__ == "__main__":
    main()
