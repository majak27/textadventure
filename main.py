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
        self.location = 'Bar (1)'
player = player()

locatie = 'locatie'
title = 'title'
description = 'description'
description2 = 'description2'
description3 = 'description3'
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
  "Bar (1)": {
    title : "Bar",
    description : "Hier kan je een drankje doen, maar om de manager te helpen zal je eerst moeten beginnen met je jas ophangen...",
    description2 : 'Je krijgt snel een obersschort toegeworpen en richting de eerste de beste tafel toegestuurd om de bestellingen op te nemen. Maar door alle stress over de soep vergeet je helemaal de bestellingen. Het restaurant krijgt slechte reviews: Slechte obers, bestelling verkeerd opgenomen". [game over]',
    description3: "Ahhh, eindelijk even relaxen na al dat harde werken voor maar 1 gerecht. Je hebt het werken in een restaurant onderschat. Je vraagt de barman om een biertje. Je vergeet even helemaal dat je nog in je werktijd zit. Even later geeft de manger je je laatste taak voor vandaag: parasols uitklappen op het buitenterras (hint: de parasols liggen in de garage).",
    opties : "N: Gang\nO: Keuken\nZ: Ingang",
    item : ['object'],
    N: "Gang",
    O: "Keuken (1)",
    Z: "Ingang (1)",
  }, 
  "Gang":{
    title : "Gang",
    description :"Je bent bij een kapstok. Handig, want je hebt nog al je waardevolle spullen in je jaszak zitten. Je hangt je jas op. Je ziet in je ooghoek een sleutel met het woord 'garage' erop staan. \nZo nu kan je aan het werk!",
    opties : "N: Keuken\nO: WC\nZ: Eetgedeelte",
    item : ["sleutel"],
    N: "Keuken (2)",
    O: "WC",
    Z: "Eetgedeelte (1)",
  },
  "Keuken (1)" : {
    title: "Keuken",
    description : "Je hebt je jas nog niet opgehangen? Je denkt toch niet met jas aan te kunnen werken? Hang je jas gewoon op joh!",
    description2: "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. Je begint met het maken van champignonsoep, maar er is geen champignon meer in de voorraadkast van de keuken. Misschien ligt er ergens anders in het restaurant nog een voorraad aan voedsel?",
    description3: "Ah, fijn! Je hebt de champignons gevonden. Je snijdt ze snel in stukjes en doet ze in de pan en begint de soep te roeren. Na een paar minuten flink geroert te hebben, giet je de soep voorzichtig op de borden. De soep wordt meteen geserveerd en valt gelukkig goed in de smaak. Er moet nu alleen nog worden afgewassen.",
    opties: "N: Bar\nO: Gang\nZ: Ingang",
    item : [],
    N: "Bar (1)",
    O: "Gang",
    Z: "Ingang (1)",
  },
  "Bijkeuken": {
    title : "Bijkeuken",
    description : "Je bent bezig met afwassen. Wanneer je alle borden grondig hebt afgewassen komt de manager blij naar je toe met 1 laatste taak voor jou vandaag. Je moet parasols op het buitenterras neerzetten (een tip: de parasols vindt je in de garage).",
    opties : "N: Bar \nO: Keuken\nZ: Garage",
    item : [],
    N: "Bar",
    O: "Keuken",
    Z: "Garage"
  },
  "Opslag": {
    title: "Opslag",
    description: "Hier is al het voorraad aan eten opgeslagen. Je kan hier het benodigde eten of drinken halen. Je hebt je champignons gevonden. Nu kan je verdergaan met je soep.",
    opties : "A: Bar\nO: Eetgedeelte \nZ: Keuken",
    item : [],
    N: "Bar (2)",
    O: "Eetgedeelte (1)",
    Z: "Keuken (3)",
  },
  "WC": {
    title : "WC",
    description: "Nou, je moet wel echt nodig... Even rustig op de wc met een boekje... Even je socials checken... Oeps, je bent de tijd vergeten... [game over]",
    opties : "",
    item : [],
    N: "",
    O: "",
    Z: ""
  },
  "Ingang (1)": {
    title: "Ingang",
    description: "Je bent nu buiten het restaurant. \nHier is geen kraan of iets om je water te vullen. \nNou ja, je stapt in je auto en rijdt van het restaurant weg... [game over]",
    opties : "",
    item: [],
    N: "",
    O: ""
  },
    "Ingang (2)": {
    title: "Ingang",
    description: "Ik neem aan dat je parasols niet voor hier binnen wil gebruiken? Ze zijn toch echt voor buiten bedoeld.",
    opties : "N: Buitenterras \nO: Garage",
    item: [],
    N: "Buitenterras",
    O: "Garage (2)",
  },
  "Ingang (3)": {
    title: "Ingang",
    description: "Je weet niet waar de garage is... Nou oké, whatever... Hier 5 euro als dank voor het doen van maar 1 klusje... Je hoeft hietr gelijk niet meer te werken. [game over]",
    opties : [] ,
    item: "",
    N: "",
    O: "",
  },
  "Eetgedeelte (1)": {
    title: "Eetgedeelte",
    description: "Oké, je hebt nog niet instructies gekregen, maar zo te zien zijn er obers nodig. Hoe moeilijk kan het nou zijn om mensen hun bestellingen op te nemen?",
    opties : "N: Bar \nO: Keuken \nZ: Ingang", 
    item: [] ,
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
  },
  "Eetgedeelte (2)": {
    title: "Eetgedeelte",
    description: "De soep is klaar en iemand moet het serveren... Er is zo te zien een tekort aan obers. Maar hoe moeilijk kan het zijn? Je loopt rechtstreeks naar de tafel die de soep heeft bestelt. ",
    opties : "N: Bar \nO: Keuken \nZ: Ingang", 
    item: [] ,
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
  },
  "Buitenterras": {
    title: "Buitenterras",
    description: "Je hebt de parasols nog niet? Je hebt ze wel eerst nodig als je ze wil gebruiken...",
    opties: [],
    item: "",
    N: "Garage",
    Z: "Ingang (3)",

  },
  "Garage": {
    title: "Garage",
    description: "Ah, mooi je hebt de garagesleutel, want zonder die sleutel kan je natuurlijk niet binnen. Nu kan je bij de berging waar de parasols voor het buitenterras liggen.",
    opties : "N: Buitenterras \nO: Ingang",
    item: [],
    N: "Buitenterras (2)",
    O: "Ingang (2)",
  },
}

bezochteKamers = []
bezochteKamers2 = []

while True:
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
    if locatie[player.location] in bezochteKamers:
      print('\n'+locatie[player.location][description2])
    elif locatie[player.location] in bezochteKamers2:
      print('\n'+locatie[player.location][description3])
    else:
      print('\n'+locatie[player.location][description])
    print(item)
    if locatie[player.location][item] != 0:
      print('\n' + str(locatie[player.location][item]))
    print('\nJe kunt hier naartoe gaan:')
    print(locatie[player.location][opties])
    print('=' * 45)
    else:
      print('\nJe kunt hier naartoe gaan:')
      print(locatie[player.location][opties])
      print('Kies uit: n, o, z, w, g(get), d(drop), i(inventory), of h(help).')
      print('=' * 45)


  #item oppakken 
  def pick_up_item():
    print('Welk item wil je oppakken?')
    print('Kies uit:' + str(locatie[player.location][item]))
    antwoord = input ('--> ')
    if antwoord.lower() in locatie[player.location][item]:
      inventory.append(antwoord)
      print(f'{antwoord} zit nu in je inventory!')
      locatie[player.location][item].remove(antwoord)
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
          locatie[player.location][item].append(antwoord.lower())
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


