from InputValidator import InputValidator
import Scraper

def main():
  foodType = input("What would you like to eat?")
  if InputValidator.ValidateInputCousine( foodType ):
    Scraper.Start()
  else:
    print("Try again")
  

  

if __name__ == "__main__":
    main()
