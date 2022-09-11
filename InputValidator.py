class InputValidator:
  def __init__(self):
        pass
  supported_cousines = ["Italian", "Indian", "Chinise"]

  @staticmethod
  def ValidateInputCousine( cousine:str ) -> bool:
    if cousine in InputValidator.supported_cousines:
      return True
    else:
      return False
    