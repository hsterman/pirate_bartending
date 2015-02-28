import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def drinkstyle():
  answers = {
    "strong": False,
    "salty": False,
    "bitter": False,
    "sweet": False,
    "fruity": False
  }
  for question in questions:
    userinput = raw_input(questions[question])
    if (userinput in ["yes", "y"]): 
      answers[question] = True
  return answers

def brewdrink(answers):
  ingredientlist = []
  for answer in answers:
    if (answers[answer] == True):
      ingredientlist.append(random.choice(ingredients[answer]))
  return ingredientlist

myanswers = drinkstyle()
myingredients = brewdrink(myanswers)
print(myingredients)