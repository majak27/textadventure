import time
import sys 
import os

#to do
# - health systeem?

#INVENTORY LIST
inventory = ['je jas']

class player:
    def __init__(self):
        self.name = ''
        self.location = 'Bar'
player = player()

locatie = 'locatie'
title = 'title'
description = 'description'
item = 'item'
lijst = 'lijst'
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
    opties : "N: Gang\nO: Keuken\nZ: Ingang",
    item : ['je jas'],
    N: "Gang",
    O: "Keuken (1)",
    Z: "Ingang",
  }, 
  "Gang":{
    title : "Gang",
    description :"Je bent bij een kapstok. Handig, want je hebt nog al je waardevolle spullen in je jaszak zitten. Je hangt je jas op. Je ziet in je ooghoek een sleutel met het woord 'garage' erop staan. \nZo nu kan je aan het werk!",
    opties : "N: Keuken\nO: WC\nZ: Eetgedeelte",
    item : ["sleutel"],
    N: "Keuken",
    O: "WC",
    Z: "Eetgedeelte",
  },
  "Keuken (1)" : {
    title: "Keuken",
    description : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. Je begint met het maken van champignonsoep, maar er is geen champignon meer in de voorraadkast van de keuken. Misschien ligt er ergens anders in het restaurant nog een voorraad aan voedsel?",
    opties : "N: Bar\nO: Opslag\nZ: Bijkeuken",
    item : "",
    N: "Bar",
    O: "Opslag",
    Z: "Bijkeuken",
  },
  "Keuken (2)": {
    title: "Keuken",
    description : "Ah, fijn! Je hebt de champignons gevonden. Je snijdt ze snel in stukjes en doet ze in de pan en begint de soep te roeren. Na een paar minuten flink geroert te hebben, giet je de soep voorzichtig op de borden. De soep kan worden geserveerd.",
    opties : "N: Eetgedeelte\nO: Bar \nZ: Bijkeuken ",
    item: "",
    N: "Eetgedeelte",
    O: "Bar",
    Z: "Bijkeuken",
  },
  "Bijkeuken": {
    title : "Bijkeuken",
    description : "Hier kan je even snel de klusjes doen die voor het koken in de keuken gedaan moeten worden zoals: afwassen, wasmachine uitruimen, keuken schoonmaken etc.",
    opties : "N: Bar \nO: Keuken",
    item : "",
    N: "Bar",
    O: "Keuken",
  },
  "Opslag": {
    title: "Opslag",
    description: "Hier is al het voorraad aan eten opgeslagen. Je kan hier het benodigde voedsel uit pakken. Ga terug naar de Keuken. ",
    opties : "A: Bar\nO: Eetgedeelte \nZ: Keuken",
    item : "",
    N: "Bar",
    O: "Eetgedeelte",
    Z: "Keuken (2)",
  },
  "WC": {
    title : "WC",
    description: "Nou, je moet wel echt nodig... Even rustig op de wc met een boekje... Even je socials checken... Oeps, je bent de tijd vergeten... [game over]",
    opties : "N: Bar\nO: Gang",
    item : "",
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
  },
  "Ingang": {
    title: "Ingang",
    description: "Je bent nu buiten het restaurant. \nHier is geen kraan of iets om je water te vullen. \nNou ja, je stapt in je auto en rijdt van het restaurant weg...",
    opties : "N: Buitenterras \nO: Garage",
    item: "",
    N: "Buitenterras",
    O: "Garage",
  },
  "Eetgedeelte": {
    title: "Eetgedeelte",
    description: "Oké, je hebt nog geen opdracht gekregen om ober te gaan spelen. Maar hè, hoe lastig kan het zijn? Beetje bestellingen opnemen, naar klanten lachen... Je loopt naar de eerste de beste tafel en je neemt de bestellingen op.",
    opties : "N: Bar \nO: Keuken \nZ: Ingang", 
    item: "",
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
  },
  "Buitenterras": {
    title: "Buitenterras",
    description: "Heb je de parasols? Zo ja? Goed bezig! Nu moet je ze uitklappen en opzetten en dan ben je klaar voor vandaag.",
    opties : "N: Ingang \nO: Garage",
    item: "",
    N: "Ingang",
    O: "Garage",
  },
  "Garage": {
    title: "Garage",
    description: "Heb je de garagesleutel? Zo ja, dan kan je in de berging van de garage met de garagesleutel. Nu kan je bij de parasols voor het buitenterras.",
    opties : "N: Buitenterras \nO: Ingang",
    item: "",
    N: "Buitenterras",
    O: "Ingang",
  },
}

if True:
  if locatie[player.location] == "keuken":
    print('hoi')

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
  print('Je bent hier: ' + player.location)
  print('\n'+locatie[player.location][description])
  print('\n' + str(locatie[player.location][item]))
  print('\nJe kunt hier naartoe gaan:')
  print(locatie[player.location][opties])
  print('=' * 45)

#item oppakken 
#! hele list wordt geplaatst in inventory, veranderen naar alleen variabele!! 
def pick_up_item():
  print('Welk item wil je oppakken?')
  print('Kies uit:' + str(locatie[player.location][item]))
  antwoord = input ('--> ')
  if antwoord.lower() in locatie[player.location][item]:
    inventory.append(antwoord)
    print(f'{antwoord} zit nu in je inventory!')
    del locatie[player.location][item]
  else:
    print('Dit is niet een geldig antwoord. Probeer opnieuw.')
    pick_up_item()
  time.sleep(1)
  game_loop()

#item droppen
def drop_item(): 
    print(inventory)
    print('Welk item wil je droppen?')
    antwoord = input('--> ')
    if antwoord in inventory:
        inventory.remove(antwoord)
        locatie[player.location][item].append(antwoord)
        print(f'{antwoord} is nu gedropt.')
        time.sleep(1)
    else:
        print(f'Je hebt {antwoord} niet in je inventory!')
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
print('Welkom bij het Restaurant Drama!\nDruk op enter om verder te gaan')
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
print('-' * 45)
print ('Gedurende het spel kun je de volgende letters intoetsen:\ni: inventory (deze is nu nog leeg!) \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nn,o,z,w: om naar verschillende ruimtes te gaan')
print('-' * 45)
print("Druk op enter om verder te gaan. ")
print('=' * 45)
iets = input()
os.system("clear")

#SCHERM4
print('=' * 45)
print(f"Je zit aan de bar met een drankje in een restaurant.\nHet is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.\nNog voordat je iets kan zeggen zegt een mannenstem:\n‘Ik betaal het drankje voor beste {naam} hier!\nHet is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.\n\nJe moet de manager helpen!")
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
    time.sleep(2)
    game_loop()

game_loop()


