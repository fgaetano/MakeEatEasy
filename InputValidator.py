"""Helper class to validate user input"""
supported_cuisines = ("italian", "indian", "thai")

class InputValidator:
  def __init__(self):
        pass

  @staticmethod
  def ValidateInputCuisine( cuisine:str ) -> bool:
    """Validate the input cuisine is included in the supported ones.
    Returns true if the input is supported, false otherwise."""
    if cuisine in supported_cuisines:
      return True
    return False
    