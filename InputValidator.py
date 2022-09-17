"""Helper class to validate user input"""
supported_cousines = ("italian", "indian", "thai")

class InputValidator:
  def __init__(self):
        pass

  @staticmethod
  def ValidateInputCousine( cousine:str ) -> bool:
    """Validate the input cousine is included in the supported ones.
    Returns true if the input is supported, false otherwise."""
    if cousine in supported_cousines:
      return True
    return False
    