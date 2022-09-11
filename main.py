from InputValidator import InputValidator

def main():
  validator = InputValidator()
  foodType = input("What would you like to eat?")
  if validator.ValidateInputCousine( foodType ):
    print("There we go")
  else:
    print("Try again")
  

  

if __name__ == "__main__":
    main()
