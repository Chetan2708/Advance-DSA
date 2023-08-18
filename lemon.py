numOfLemon = 25
print("Invalid input" if type(numOfLemon) != type(1) else "enough lemon" if numOfLemon ==
      21 else f"we need {21-numOfLemon }  lemons" if numOfLemon < 21 and numOfLemon >= 0 else f"we have {numOfLemon -21 } extra lemons" if numOfLemon > 21 else "Num cannot be less than 0")
