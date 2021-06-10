import time
import sys 
import os
from locations import locatie

#INVENTORY
inventory = ['','jas']

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
descriptionItems = 'descriptionItems'
descriptionItems2 = 'descriptionItems2'
gameOver = 'gameOver' 
nodig = 'nodig'
N = 'n'
O = 'o'
Z = 'z'
W = 'w'

os.system('clear')
def typewriter():
  if effect.lower().strip() == 's':
    for char in text: 
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep (0.02)
  elif effect.lower().strip() == 'l':
    for char in text: 
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep (0.05)
  elif effect.lower().strip() == 'g':
    print(text)
  else:
    print('Geen geldige optie probeer opnieuw')
    time.sleep(2)
    typewriter()

#animatie opties
print('=' * 45)
print('Voor we beginnen; wil je: \n(s) snelle animaties,\n(l) langzame animaties\n(g) geen animaties')
print('=' * 45)
effect = input('--> ')
text = ''
typewriter() 

#SCHERM1
os.system('clear')
print('=' * 45)
text = 'Welkom bij het Restaurant Drama!\nDruk op enter om verder te gaan'
typewriter()
input()
os.system('clear')

#SCHERM2
print('=' * 45)
text = 'Wat is je naam?\n'
typewriter()
player.name = input('--> ')
os.system("clear")

#SCHERM3
print('=' * 45)
text = f"Hallo {player.name}, welkom bij het spel!\n{'-' * 45 }\nGedurende het spel kun je de volgende letters intoetsen:\ni: inventory \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nd: drop (om een item neer te leggen)\nq: quit (om te stoppen)\nn,o,z,w: om naar verschillende ruimtes te gaan\n\nLet op! Je antwoorden mogen maar 1 letter lang zijn (behalve bij het kiezen van een object)\n"
typewriter()
print('-' * 45)
print("Druk op enter om verder te gaan. ")
print('=' * 45)
input()
os.system("clear")

#SCHERM4
print('=' * 45)
text = f"Je zit aan de bar met een drankje in een restaurant.\nHet is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.\nNog voordat je iets kan zeggen zegt een mannenstem:\n‘Ik betaal het drankje voor beste {player.name} hier!\nHet is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.\n\nJe moet de manager helpen!\n\nHet doel van het spel is om de 3 taken te vinden op verschillende locaties en deze uit te voeren. Heb je dat succesvol gedaan, heb je gewonnen! Succes :)\n"
typewriter()
print('=' * 45)
print("Druk op enter om de manager te helpen met zijn taken")
input()
os.system('clear')

while True:
  itemDingetjes = []
  #help
  def help_menu(): 
    os.system("clear")
    print('=' * 45)
    print('HELP!')
    print('=' * 45)
    print('Het doel van het spel is om de juiste objecten\nte vinden door langs verschillende locaties langs te gaan.\n')
    print('Let op! Je antwoorden kunnen maar 1 letter lang zijn (behalve wanneer je een item kiest.)\n')
    print('\ni: inventory \nh: help (voor als je het even niet meer weet)\ng: get (om een item op te pakken)\nd: drop (om een item neer te leggen)\nq: quit (om te stoppen)\nn,o,z,w: om naar verschillende ruimtes te gaan')
    print("\nDruk op 'b' om terug te gaan")
    print('=' * 45)
    inventory_opties()

  #inventory
  def inventory_menu():
    os.system("clear")
    print('=' * 45)
    print("Dit zit nu in je inventory:\n")
    for x in inventory:
      if x != '':
        print('*'+ x)
    print('\nEr zijn 3 opdrachten in totaal. Hieronder staan de taken die je hebt gevonden:')
    if 'bestelling' in inventory:
      print('* bestelling: Zoek naar een glas water en lever het bij het eetgedeelte.')
    if 'parasol taak' in inventory:
      print('* parasol taak: Zoek naar de parasols en breng ze naar het buitenterras.')
    if 'champignon taak' in inventory:
      print('* champignon taak: Zoek de champignons en breng ze naar de keuken.')
    print("\nDruk op 'b' om terug te gaan")
    print('=' * 45)
    inventory_opties()

  def inventory_opties():
    antwoord = input('--> ')
    if antwoord.lower().strip() == "b":
      game_loop()
    else:
      print("Sorry, dit is niet een geldige antwoord, probeer opnieuw.")
    inventory_opties()

  #terug kunnen gaan bij menu
  def menu_opties():
    antwoord = input('--> ')
    if antwoord.lower().strip() == "j":
      game_over()
    if antwoord.lower().strip() == "b":
      print_location()
    else:
      print("Sorry, dit is niet een geldig antwoord, probeer opnieuw.")
      menu_opties()

  def nog_nodig():
    os.system('clear')
    print('Je hebt het benodigde item nog niet, dus kan je deze ruimte niet binnen.')
    print(f'Zoek naar {locatie[player.location][nodig]} en kom hier terug!')
    print("Druk op 'b' om terug naar de bar te gaan.")
    player.location = 'Bar'
    menu_opties()
  
  #toont je locatie
  def print_location():
    if locatie[player.location][gameOver] == 'ja':
      game_over_locatie()
    elif locatie[player.location][nodig] not in inventory:
      nog_nodig()
    else:
      os.system('clear')
      print('=' * 45)
      print('Je bent hier: ' + player.location)
      if locatie[player.location][descriptionItems] in inventory or locatie[player.location][descriptionItems] in itemDingetjes:
        itemDingetjes.append(locatie[player.location][descriptionItems])
        print('\n'+locatie[player.location][description2])
      elif locatie[player.location][descriptionItems2] in inventory:
        print('\n'+locatie[player.location][description3])
      else:
        print('\n'+locatie[player.location][description])
      if locatie[player.location][item] != 0:
        print("\nHier ligt:")
        for x in locatie[player.location][item]:
          print('* ' + x)
      print('\nJe kunt hier naartoe gaan:')
      print(locatie[player.location][opties])
      print('\nKies uit: n, o, z, w, g(get), d(drop), i(inventory), h(help) of q(quit).')
      print('=' * 45)

  #item oppakken 
  def pick_up_item():
    print('Welk item wil je oppakken?')
    print('Kies uit:' + str(locatie[player.location][item]))
    antwoord = input ('--> ')
    #if antwoord.lower()
    if antwoord.lower().strip() in locatie[player.location][item]:
      inventory.append(antwoord.lower())
      print(f'{antwoord} zit nu in je inventory!')
      locatie[player.location][item].remove(antwoord.lower().strip())
      game_loop()
    else:
      print('Dit is niet een geldig antwoord. Probeer opnieuw.')
      time.sleep(1)
      pick_up_item()

  #item droppen
  def drop_item(): 
    print(inventory)
    print('Welk item wil je droppen?')
    antwoord = input('--> ')
    if antwoord.lower().strip() in inventory:
      inventory.remove(antwoord.lower())
      locatie[player.location][item].append(antwoord.lower())
      print(f'{antwoord} is nu gedropt.')
      game_loop()
    else:
      print(f'Je hebt {antwoord.lower()} niet in je inventory! Probeer opnieuw.')
      time.sleep(2)
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

  #win scherm
  def win():
    os.system('clear')
    print('=' * 45)
    print('JE HEBT DE TAAK VOLTOOID!')
    print('=' * 45)
    time.sleep(5)
    os.system('clear')
   
  def game_over():
    os.system('clear')
    print('=' * 45)
    print('GAME OVER')
    print('=' * 45)
    time.sleep(5)
    os.system('clear')

  #game over scherm
  def game_over_locatie():
    os.system('clear')
    print('=' * 45)
    print('Je bent hier: ' + player.location)
    print('\n'+locatie[player.location][description])
    print('=' * 45)
    print('Druk op enter om verder te gaan.')
    input()
    game_over()

  #GAMELOOP
  def game_loop():
    if "glas water" in locatie['Eetgedeelte'][item] and 'champignons' in locatie['Keuken'][item] and 'parasols' in locatie['Buitenterras'][item]:
      win()
    else:
      print_location()
      nextRoom = input('--> ')
      if nextRoom.lower().strip() == "h":
        help_menu()
      elif nextRoom.lower().strip() == "g":
        pick_up_item()
      elif nextRoom.lower().strip() == "d":
        drop_item()
      elif nextRoom.lower().strip() == "i":
        inventory_menu()
      elif nextRoom.lower().strip() == "q":
        stop_screen()
      elif nextRoom.lower().strip() == 'n':
        move_actie = locatie[player.location][N]
        move_speler(move_actie)
      elif nextRoom.lower().strip() == 'o':
        move_actie = locatie[player.location][O]
        move_speler(move_actie)
      elif nextRoom.lower().strip() == 'z':
        move_actie = locatie[player.location][Z]
        move_speler(move_actie)
      elif nextRoom.lower().strip() == 'w':
        move_actie = locatie[player.location][W]
        move_speler(move_actie)
      else:
        print('Sorry, dit is niet een geldige optie, probeer opnieuw')
        time.sleep(2)
        game_loop()
  
  game_loop()


