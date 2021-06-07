import time
import sys 
import os
from locations import locatie

#to do
# als er een locatie niet is, niet mogelijk om daarnaartoe te gaan
# probleem: als je meteen op enter drukt bij de eerste locatie ga je al door naar de volgende?

#INVENTORY
inventory = ['jas']

class player:
    def __init__(self):
        self.name = ''
        self.location = 'Bar'
player = player()

title = 'title'
description = 'description'
description2 = 'description2'
description3 = 'description3'
item = 'item'
lijst = 'lijst'
opties = 'opties'
gameOver = 'gameOver' 
nodig = 'nodig'
N = 'n'
O = 'o'
Z = 'z'
W = 'w'

#SCHERM1
print('=' * 45)
print('Welkom bij het Restaurant Drama!\nDruk op enter om verder te gaan')
antwoord = input()
os.system('clear')

#SCHERM2
print('=' * 45)
print('Wat is je naam?')
player.name = input('--> ')
os.system("clear")

#SCHERM3
print('=' * 45)
print(f"Hallo {player.name}, welkom bij het spel!")
print('-' * 45)
print ('Gedurende het spel kun je de volgende letters intoetsen:\ni: inventory \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nd: drop (om een item neer te leggen\nq: quit (om te stoppen)\nn,o,z,w: om naar verschillende ruimtes te gaan')
print('-' * 45)
print("Druk op enter om verder te gaan. ")
print('=' * 45)
iets = input()
os.system("clear")

#SCHERM4
print('=' * 45)
print(f"Je zit aan de bar met een drankje in een restaurant.\nHet is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.\nNog voordat je iets kan zeggen zegt een mannenstem:\n‘Ik betaal het drankje voor beste {player.name} hier!\nHet is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.\n\nJe moet de manager helpen!")
print('=' * 45)
print("Druk op enter om de manager te helpen met zijn taken")
antwoord = input()
os.system('clear')

while True:
  bezochteKamers = []
  bezochteKamers2 = []

  #help
  def help_menu(): 
    os.system("clear")
    print('=' * 45)
    print('HELP!')
    print('=' * 45)
    print('Het doel van het spel is om de juiste objecten\nte vinden door langs verschillende locaties langs te gaan.\n')
    print('Let op! Je antwoorden kunnen maar 1 letter lang zijn')
    print('\ni: inventory \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nd: drop (om een item neer te leggen)\nq: quit (om te stoppen)\nn,o,z,w: om naar verschillende ruimtes te gaan')
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
    inventory_opties()

  def inventory_opties():
    if locatie[player.location] in bezochteKamers:
      bezochteKamers.remove(locatie[player.location])
    elif locatie[player.location] in bezochteKamers2:
      bezochteKamers2.remove(locatie[player.location])
    if 'bestelling' in inventory:
      print('Wil je de bestelling bekijken?')
    antwoord = input('--> ')
    if antwoord.lower() == "j":
      print('Een glas water voor het eetgedeelte.')
    elif antwoord.lower() == "b":
      print_location()
    else:
      print("Sorry, dit is niet een geldige antwoord, probeer opnieuw.")
      menu_opties()

  #terug kunnen gaan bij menu
  def menu_opties():
    if locatie[player.location] in bezochteKamers:
      bezochteKamers.remove(locatie[player.location])
    elif locatie[player.location] in bezochteKamers2:
      bezochteKamers2.remove(locatie[player.location])
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
    if locatie[player.location][nodig] not in inventory:
      print(f'Je moet {locatie[player.location][nodig]} hebben om naar deze locatie te gaan.')
    if locatie[player.location][gameOver] == 'ja':
      game_over()
    else:
      os.system('clear')
      print('=' * 45)
      print('Je bent hier: ' + player.location)
      if locatie[player.location] in bezochteKamers:
        print('\n'+locatie[player.location][description2])
        bezochteKamers2.append(locatie[player.location])
      elif locatie[player.location] in bezochteKamers2:
        print('\n'+locatie[player.location][description3])
      else:
        print('\n'+locatie[player.location][description])
        bezochteKamers.append(locatie[player.location])
      if locatie[player.location][item] != 0:
        print("\nHier ligt:")
        for x in locatie[player.location][item]:
          print('* ' + x)
      print('\nJe kunt hier naartoe gaan:')
      print(locatie[player.location][opties])
      print('\nKies uit: n, o, z, w, g(get), d(drop), i(inventory), of h(help).')
      print('=' * 45)

  #item oppakken 
  def pick_up_item():
    print('Welk item wil je oppakken?')
    print('Kies uit:' + str(locatie[player.location][item]))
    antwoord = input ('--> ')
    if antwoord.lower() in locatie[player.location][item]:
      inventory.append(antwoord.lower())
      print(f'{antwoord} zit nu in je inventory!')
      locatie[player.location][item].remove(antwoord.lower())
      if locatie[player.location] in bezochteKamers:
        bezochteKamers.remove(locatie[player.location])
      elif locatie[player.location] in bezochteKamers2:
        bezochteKamers2.remove(locatie[player.location])
      print_location()
    else:
      print('Dit is niet een geldig antwoord. Probeer opnieuw.')
      time.sleep(1)
      pick_up_item()

  #item droppen
  def drop_item(): 
    print(inventory)
    print('Welk item wil je droppen?')
    antwoord = input('--> ')
    if antwoord.lower() in inventory:
      inventory.remove(antwoord.lower())
      locatie[player.location][item].append(antwoord.lower())
      print(f'{antwoord} is nu gedropt.')
      if locatie[player.location] in bezochteKamers:
        bezochteKamers.remove(locatie[player.location])
      elif locatie[player.location] in bezochteKamers2:
        bezochteKamers2.remove(locatie[player.location])
        print_location()
    else:
      print(f'Je hebt {antwoord.lower()} niet in je inventory! Probeer opnieuw.')
      drop_item()
    
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
      print('Sorry, dit is niet een geldige optie, probeer opnieuw')
      game_loop()
  
  game_loop()


