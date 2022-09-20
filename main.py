from InputValidator import InputValidator
import Scraper

def main():
  foodType = input("What would you like to eat? ")
  if InputValidator.ValidateInputCousine( foodType ):
    Scraper.Start(foodType)
  else:
    print("Invalid input. Terminating.")
  

  

if __name__ == "__main__":
    main()
