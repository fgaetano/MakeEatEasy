from InputValidator import InputValidator

def main():
  foodType = input("What would you like to eat?")
  if InputValidator.ValidateInputCousine( foodType ):
    print("There we go")
  else:
    print("Try again")
  

  

if __name__ == "__main__":
    main()
