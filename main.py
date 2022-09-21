from InputValidator import InputValidator
import Scraper


def main():
    foodType = input("What would you like to eat? ")
    if InputValidator.ValidateInputCousine(foodType):
        kws = list()
        print("What do you have in your fridge? (insert 's' to terminate")
        kw = input()
        while kw != "s":
            kws.append(kw)
            kw = input()
        Scraper.Start(foodType, kws)

    else:
        print("Invalid cousine. Terminating.")


if __name__ == "__main__":
    main()
