import time
import sys 
import os
from tabulate import tabulate

#to do
# - health systeem?
print(1)

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
item = 'item'
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
    description : "Hier kan je een drankje doen, maar om de manager te helpen zal je eerst moeten beginnen met je jas ophangen...",
    opties : "N: Gang\nO: Keuken\nZ: Ingang\nW: ..",
    item : ['object'],
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
    W: ""
  }, 
  "Gang":{
    title : "Gang",
    description :"Je bent bij een kapstok. Handig, want je hebt nog al je waardevolle spullen in je jaszak zitten. Je hangt je jas op. Je ziet in je ooghoek een sleutel met het woord 'garage' erop staan.",
    opties : "N: Bar\nO: WC\nZ: Eetgedeelte\nW: ..",
    item : "",
    N: "Bar",
    O: "WC",
    Z: "Eetgedeelte",
    W: ""
  },
  "Keuken" : {
    title: "Keuken",
    description : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood.",
    opties : "N: Bar\nO: Opslag\nZ: Bijkeuken\nW:...",
    item : "Glas",
    N: "Bar",
    O: "Opslag",
    Z: "Bijkeuken",
    W: ""
  },
  "Bijkeuken": {
    title : "Bijkeuken",
    description : "",
    opties : "N: Bar \nO: Keuken\nZ: .. \n W: ..",
    item : "",
    N: "Bar",
    O: "Keuken",
    Z: "",
    W: ""
  },
  "Opslag": {
    title: "Opslag",
    description: "locatie5",
    opties : "A: Bar\nO: Eetgedeelte \nZ: Keuken\nW:...",
    item : "",
    N: "Bar",
    O: "Eetgedeelte",
    Z: "Keuken",
    W: ""
  },
  "WC": {
    title : "WC",
    description: "description",
    opties : "N: Bar\nO: Gang",
    item : "",
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
    W: ""
  },
  "Ingang": {
    title: "Ingang",
    description: "Je bent nu buiten het restaurant. \nHier is geen kraan of iets om je water te vullen. \nNou ja, je stapt in je auto en rijdt van het restaurant weg...",
    opties : "N: Buitenterras \nO: Garage",
    N: "Buitenterras",
    O: "Garage",
    Z: "",
    W: ""
  },
  "Eetgedeelte": {
    title: "Eetgedeelte",
    description: "locatie8",
    opties : "N: Bar \nO: Ingang",
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
    W: ""
  },
  "Buitenterras": {
    title: "Buitenterras",
    description: "locatie9",
    opties : "N: Ingang \nO: Garage",
    N: "Ingang",
    O: "Garage",
    Z: "",
    W: ""
  },
  "Garage": {
    title: "Garage",
    description: "locatie10",
    opties : "N: Buitenterras \nO: Ingang",
    N: "Buitenterras",
    O: "Ingang",
    Z: "",
    W: ""
  },
}

ding = locatie[player.location][item]

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

#terug kunnen gaan bij menu's
def menu_opties():
  antwoord = input('--> ')
  if antwoord.lower() == "j":
    game_over()
  if antwoord.lower() == "b":
    print_location()
  else:
    print("Sorry, dit is niet een geldige antwoord, probeer opnieuw.")
    menu_opties()

#toont je locatie
def print_location():
  os.system('clear')
  print('=' * 45)
  print(player.location)
  print('\n'+locatie[player.location][description])
  print('\nJe kunt hier naartoe gaan:')
  print(locatie[player.location][opties])
  print('=' * 45)

#item oppakken (!je kan hierna nog niet naar een andere kamer)
def pick_up_item():
  print(f'{ding} zit nu in je inventory!')
  inventory.append(ding)
  del locatie[player.location][item]
  time.sleep(1)
  game_loop()

#item droppen
#nog doen: toevoegen aan item van de ruimte zelf
def drop_item(): 
  print(list(enumerate(inventory)))
  print('Welk item wil je droppen?')
  antwoord = int(input('--> '))
  voorwerp = inventory[antwoord]
  inventory.remove(voorwerp)
  locatie[player.location][item].append(voorwerp)
  print(f'{voorwerp} is nu gedropt.')
  time.sleep(1)
  game_loop()
  
#naar andere ruimtes gaan
def move_speler(move_actie):
	player.location = move_actie
	game_loop()

#quit scherm
def stop_screen():
  os.system('clear')
  print('=' * 45)
  print('STOP')
  print("\nWil je het spel beëindigen? Druk op 'j'\nWil je terug naar het spel? Druk op 'b'\n")
  print('=' * 45)
  menu_opties()

#game over scherm
def game_over():
  os.system('clear')
  print('=' * 45)
  print('GAME OVER')
  print('=' * 45)
  time.sleep(4)
  sys.exit()

#SCHERM1
print('=' * 45)
scherm1 = 'Welkom bij het Restaurant Drama!\nDruk op enter om verder te gaan\n'
for char in scherm1:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.04)
antwoord = input()
os.system('clear')

#SCHERM2
print('=' * 45)
scherm2 = 'Wat is je naam?\n'
for char in scherm2:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.04)
naam = input('--> ')
os.system("clear")

#SCHERM3
print('=' * 45)
scherm3 = f"Hallo {naam}, welkom bij het spel!\n"
for char in scherm3:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.04)
table = [["Gedurende het spel kun je de volgende letters intoetsen:\ni: inventory (deze is nu nog leeg!) \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nn,o,z,w: om naar verschillende ruimtes te gaan"]]
print(tabulate(table, tablefmt='grid'))
print("Druk op enter om verder te gaan. ")
print('=' * 45)
iets = input()
os.system("clear")

#SCHERM4
print('=' * 45)
scherm4 = f"Je zit aan de bar met een drankje in een restaurant.\nHet is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.\nNog voordat je iets kan zeggen zegt een mannenstem:\n‘Ik betaal het drankje voor beste {naam} hier!\nHet is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.\nJe moet de manager helpen!\n"
for char in scherm4:
  sys.stdout.write(char)
  sys.stdout.flush()
  time.sleep(0.02)
print('=' * 45)
print("Druk op enter om de manager te helpen met zijn taken")
antwoord = input()
os.system('clear')

#GAMELOOP
def game_loop():
  print_location()
  nextRoom = input('--> ')
  if nextRoom.lower() == "h":
    help_menu()
  elif nextRoom.lower() == "g":
    pick_up_item()
  elif nextRoom.lower() == "d":
    drop_item()
  elif nextRoom.lower() == "i":
    inventory_menu()
  elif nextRoom.lower() == "q":
    stop_screen()
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


