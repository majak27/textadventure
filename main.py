import time
import os
from tabulate import tabulate

#INVENTORY LIST
inventory = []

class player:
    def __init__(self):
        self.name = ''
        self.location = 'Bar'
player = player()


locatie = 'locatie'
title = 'title'
description = 'description'
items = 'items'
opties = 'opties'
dood = 'dood'
win = 'win'
N = 'n'
O = 'o'
Z = 'z'
W = 'w'

#LOCATIES
locatie = {
  "Bar": {
    title : "Bar",
    description : "Je kan hier een drankje doen.",
    opties : "N: Gang\nO: Keuken\nZ: Ingang\nW: ..",
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
    W: ""
  }, 
  "Gang":{
    title : "Gang",
    description :"Je bent bij een kapstok. Handig, want je had je jas nog aan met alles op zak zoals je telefoon, portemonnee etc. kan je niet goed werken. Je hangt je jas op.",
    opties : "N: Bar\nO: WC\nZ: Eetgedeelte\nW: ..",
    N: "Bar",
    O: "WC",
    Z: "Eetgedeelte",
    W: ""
  },
  "Keuken" : {
    title: "Keuken",
    description : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. ",
    opties : "N: Bar\nO: Opslag\nZ: Bijkeuken\nW:...",
    N: "Bar",
    O: "Opslag",
    Z: "Bijkeuken",
    W: ""
  },
  "Bijkeuken": {
    title : "Bijkeuken",
    description : "Je kan hier iets doen",
    opties : "N: Bar \nO: Keuken\nZ: .. \n W: ..",
    N: "Bar",
    O: "Keuken",
    Z: "",
    W: ""
  },
  "Opslag": {
    title: "Opslag",
    description: "locatie5",
    opties : "A: Bar\nO: Eetgedeelte \nZ: Keuken\nW:...",
    N: "Bar",
    O: "Eetgedeelte",
    Z: "Keuken",
    W: ""
  },
  "WC": {
    title : "WC",
    description: "description",
    opties : "N: Bar\nO: Gang",
    N: "gang",
    O: "keuken",
    Z: "ingang",
    W: ""
  },
  "Ingang": {
    title: "Ingang",
    description: "Je bent nu buiten het restaurant. \nHier is geen kraan of iets om je water te vullen. \nNou ja, je stapt in je auto en rijdt van het restaurant weg...",
    opties : "N: Buitenterras \nO: Garage",
    N: "gang",
    O: "keuken",
    Z: "ingang",
    W: ""
  },
  "Eetgedeelte": {
    title: "Eetgedeelte",
    description: "locatie8",
    opties : "N: Bar \nO: Ingang",
    N: "gang",
    O: "keuken",
    Z: "ingang",
    W: ""
  },
  "Buitenterras": {
    title: "Buitenterras",
    description: "locatie9",
    opties : "N: Ingang \nO: Garage",
    N: "gang",
    O: "keuken",
    Z: "ingang",
    W: ""
  },
  "Garage": {
    title: "Garage",
    description: "locatie10",
    opties : "N: Buitenterras \nO: Ingang",
    N: "gang",
    O: "keuken",
    Z: "ingang",
    W: ""
  },
}

#help
def help_menu(): 
  os.system("clear")
  print('=' * 45)
  print('HELP!')
  print('=' * 45)
  print('Het doel van het spel is om de juiste objecten\nte vinden door langs verschillende locaties langs te gaan.\n')
  print('Let op! Je antwoorden kunnen maar 1 letter lang zijn')
  print('\ni: inventory (deze is nu nog leeg!) \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nn,o,z,w: om naar verschillende ruimtes te gaan')
  print("\nDruk op 'b' om terug te gaan")
  print('=' * 45)
  menu_opties()

#inventory
def inventory_menu():
  os.system("clear")
  print('=' * 45)
  print("Dit zit nu in je inventory:")
  print(inventory)
  print("\nDruk op 'b' om terug te gaan")
  print('=' * 45)
  menu_opties()

def menu_opties():
  antwoord = input('--> ')
  if antwoord.lower() == ("b"):
    print_location()
  else:
    print("Sorry, dit is niet een geldige ruimte, probeer opnieuw")
    menu_opties()

#toont je locatie
def print_location():
  os.system('clear')
  print('=' * 45)
  print(player.location)
  print(locatie[player.location][description])
  print('Je kunt hier naartoe gaan:')
  print(locatie[player.location][opties])
  print('=' * 45)

def move_speler(move_actie):
	player.location = move_actie
	print_location()

#SCHERM1
print('=' * 45)
print('Welkom bij het Restaurant Drama!')
print('Druk op enter om verder te gaan')
print('=' * 45)
antwoord = input()
os.system('clear')

#SCHERM2
print('=' * 45)
print('Wat is je naam?')
naam = input('--> ')
os.system("clear")

#SCHERM3
print('=' * 45)
print(f"Hallo {naam}, welkom bij het spel!")
table = [["Gedurende het spel kun je de volgende letters intoetsen:\ni: inventory (deze is nu nog leeg!) \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nn,o,z,w: om naar verschillende ruimtes te gaan"]]
print(tabulate(table, tablefmt='grid'))
print("Druk op enter om verder te gaan. ")
print('=' * 45)
iets = input()
os.system("clear")

#SCHERM4
print('=' * 45)
print(f"Je zit aan de bar met een drankje in een restaurant.\nHet is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.\nNog voordat je iets kan zeggen zegt een mannenstem:\n‘Ik betaal het drankje voor beste {naam} hier!\nHet is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.\nJe moet de manager helpen!")
print('=' * 45)
print("Druk op enter om de manager te helpen met zijn taken")
antwoord = input("--> ")
os.system('clear')

#Game loop
print_location()

def game_loop():
  nextRoom = input('--> ')
  if nextRoom == "h":
    help_menu()
  elif nextRoom == "i":
    inventory_menu()
  elif nextRoom.lower() == 'n':
    move_actie = locatie[player.location][N]
    move_speler(move_actie)
  elif nextRoom.lower() == 'o':
    move_actie = locatie[player.location][O]
    move_speler(move_actie)
  elif nextRoom.lower() == 'z':
    move_actie = locatie[player.location][Z]
    move_speler(move_actie)
  elif nextRoom.lower() == 'w':
    move_actie = locatie[player.location][W]
    move_speler(move_actie)
  else:
    print('Sorry, dit is niet een geldige ruimte, probeer opnieuw')
    game_loop()

game_loop()


