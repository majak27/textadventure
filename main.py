import time
import os
from tabulate import tabulate

#dictionary van locaties
locatie = {
  "bar" :  {
    "title" : "bar",
    "description" : "Je kan hier een drankje doen.",
    "opties" : "gang"
  },
  "gang":{
    "title": "gang",
    "description" :"Je bent bij een kapstok. Handig, want je had je jas nog aan, en met alles op zak zoals je telefoon, portemonnee etc. kan je niet goed werken. Je hangt je jas op. Nu kan je je melden bij de keuken.",
    "opties" : "gang"
  },
  "keuken" : {
    "title": "keuken",
    "description" : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. ",
    "opties" : "gang"
  },
  "bijkeuken": {
    "title" : "bijkeuken",
    "description": "Je kan hier iets doen",
    "opties" : "gang"
  },
  "opslag": {
    "title": "opslag",
    "description": "locatie5",
    "opties" : "gang"
  },
  "wc's": {
    "title": "wc's",
    "description": "locatie6",
    "opties" : "gang"
  },
  "ingang/uitgang": {
    "title": "ingang/uitgang",
    "description": "locatie7",
    "opties" : "gang"
  },
  "eetgedeelte": {
    "title": "eetgedeelte",
    "description": "locatie8",
    "opties" : "gang"
  },
  "buitenterras": {
    "title": "buitenterras",
    "description": "locatie9",
    "opties" : "gang"
  },
  "garage": {
    "title": "garage",
    "description": "locatie10",
    "opties" : "gang"
  }
}

#INVENTORY LIST
inventory = []

table = [["Welkom bij het Restaurant Drama!"]]
print(tabulate(table, tablefmt='grid'))
print("Druk op enter om verder te gaan")
antwoord = input()
os.system('clear')

#INTRODUCTIE
naam = input("Wat is je naam? ")
print(f"Hallo {naam}, welkom bij het spel!")
table = [["Gedurende het spel kun je naast de kamers de volgende letters intoetsen:\ni: inventory (deze is nu nog leeg!) \nh: help (voor als je het even niet meer weet)"]]
print(tabulate(table, tablefmt='grid'))
helpmenu = input("Type 'h' voor het help menu ")
if helpmenu.lower() == "h":
  table = [['Antwoorden zijn maar 1 letter lang,\nandere antwoorden worden dus ook niet geaccepteerd.\n(bv. ja = j, nee = n)\nOm je taak goed uit te voeren moet je de locaties langs om de juiste objecten te vinden.']]
  print(tabulate(table, tablefmt='grid'))
else:
  print('Niet de correcte letter... Probeer het opnieuw.')
  helpmenu = input("Type 'h' voor het help menu ")
iets = input("Druk op enter om te beginnen met het spel. ")
os.system("clear")


#BEGIN SPEL (introductie)
print("Je zit aan de bar met een drankje in een restaurant.") 
time.sleep(1.5)
print("Het is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.")
time.sleep(2)
print("Nog voordat je iets kan zeggen zegt een mannenstem:") 
print(f"‘Ik betaal het drankje voor beste {naam} hier!’")
time.sleep(2)
print ("Het is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.")
time.sleep(1.5)
print("Je moet de manager helpen!" )
print("Wil jij de manager helpen door middel van het voltooien van taken in en rondom het restaurant? (j/n)")
antwoord = input()
os.system('clear')

while True:
  if antwoord.lower().strip() == "j":
    table = [["De manager is nu al ontzettend tevreden met jou en je spontane hulp.\nHij biedt je zelfs salaris aan als je de taken goed uitvoert. \nJe (eerste) opdracht is een glas water vullen!"]]
    print(tabulate(table, tablefmt='grid'))
    #DE GAMELOOP
    def game(room):
      currentlocatie = locatie[room]
      #DE HUIDIGE RUIMTE EN DESCRIPTIE BENOEMEN
      title = currentlocatie["title"]
      description = currentlocatie["description"]
      opties = currentlocatie["opties"]
      #GEEFT AAN WAAR JE BENT
      print(f"Je bent hier: {title}")
      print(description)
      print("Type de naam van de kamer waar je naartoe wilt gaan:")
      #TOONT ALLE MOGELIJKE LOCATIES
      print(opties)
      nextRoom = input()
      os.system("clear")
      #OPDRACHT IN DE KEUKEN
      #alleen als glas nog niet in inventory is
      if nextRoom == "keuken":
        table = [['Er staat hier een glas, wil je die oppakken? (j/n)']]
        print(tabulate(table, tablefmt='grid'))
        oppakken = input()
        if oppakken.lower().strip() == 'j':
          inventory.append("glas")
          print('Het item zit nu in je inventory')
          print("Type de naam van de kamer waar je naartoe wilt gaan:")
          print(", ".join(locatie.keys()))
          nextRoom = input()
        else:
          print("Oke, type dan maar de naam van de kamer waar je naartoe wilt gaan:")
          print(", ".join(locatie.keys()))
          nextRoom = input()
          game(nextRoom)
      #INPUT CONTROL
      if nextRoom.lower().strip() not in currentlocatie["opties"]:
        print("Sorry, dit is niet een geldige ruimte, probeer opnieuw")
        print("Type de naam van de kamer waar je naartoe wilt gaan:")
        print(", ".join(locatie.keys()))
        nextRoom = input()
        game(nextRoom)
      else:
        #NAAR DE VOLGENDE RUIMTE
        game(nextRoom)
        #DE GAME START BIJ DE BAR
    game("bar")
        
  elif antwoord.lower().strip() == "n":
    antwoord = input("De manager had dit niet verwacht. Hij had je als een behulpzaam persoon ingeschat, maar dit valt hem zeer tegen. Je bent nooit meer welkom in zijn restaurant. Een maand later zie je in de krant dat het restaurant failliet is. [GAME O]").lower().input()
  else: 
    print(f"{antwoord} is niet een geldige optie, {naam}. Probeer opnieuw") 
    antwoord = input()