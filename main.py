import time
import os
from tabulate import tabulate

#INVENTORY LIST
inventory = []

#dictionary van locaties
locatie = {
  "a": {
    "title" : "Bar",
    "description" : "Je kan hier een drankje doen.",
    "opties" : "b: Gang \nc: Keuken \ng: Ingang"
  }, 
  "b":{
    "title": "Gang",
    "description" :"Je bent bij een kapstok. Handig, want je had je jas nog aan, en met alles op zak zoals je telefoon, portemonnee etc. kan je niet goed werken. Je hangt je jas op.",
    "opties" : "Keuken"
  },
  "c" : {
    "title": "Keuken",
    "description" : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. ",
    "opties" : "gang"
  },
  "d": {
    "title" : "Bijkeuken",
    "description": "Je kan hier iets doen",
    "opties" : "gang"
  },
  "e": {
    "title": "Opslag",
    "description": "locatie5",
    "opties" : "gang"
  },
  "f": {
    "title": "WC",
    "description": "locatie6",
    "opties" : "gang"
  },
  "g": {
    "title": "Ingang",
    "description": "Je bent nu buiten het restaurant. \nHier is geen kraan of iets om je water te vullen. \nNou ja, je stapt in je auto en rijdt van het restaurant weg...",
    "opties" : "gang"
  },
  "h": {
    "title": "Eetgedeelte",
    "description": "locatie8",
    "opties" : "gang"
  },
  "i": {
    "title": "Buitenterras",
    "description": "locatie9",
    "opties" : "gang"
  },
  "j": {
    "title": "Garage",
    "description": "locatie10",
    "opties" : "gang"
  },
  "m" : {
    "title": "Hulp menu",
    "description" : 'Let op je antowoorden kunnen maar 1 letter lang zijn!\n(bv. ja = j, nee = n)\nOm je taak goed uit te voeren moet je de locaties langs om de juiste objecten te vinden.',
    "opties" : "a: Bar"
  },
  "v" : {
    "title": "Inventory",
    "description": inventory ,
    "opties": "a: Bar"
  }
}


table = [["Welkom bij het Restaurant Drama!"]]
print(tabulate(table, tablefmt='grid'))
print("Druk op enter om verder te gaan")
antwoord = input()
os.system('clear')

#INTRODUCTIE
naam = input("Wat is je naam? ")
print(f"Hallo {naam}, welkom bij het spel!")
table = [["Gedurende het spel kun je naast de kamers de volgende letters intoetsen:\nv: inventory (deze is nu nog leeg!) \nm: help (voor als je het even niet meer weet)"]]
print(tabulate(table, tablefmt='grid'))
helpmenu = input("Type 'm' voor het help menu ")
if helpmenu.lower() == "m":
  table = [['Let op je antowoorden kunnen maar 1 letter lang zijn!\n(bv. ja = j, nee = n)\nOm je taak goed uit te voeren moet je de locaties langs om de juiste objecten te vinden.']]
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
      
      if currentlocatie == "m":
        print(title)
        print(description)
        print("Type de naam van de kamer waar je naartoe wilt gaan:")
        print(opties)
        nextRoom = input()
        os.system("clear")
      if currentlocatie == "v":
        print(title)
        print(f"Dit is wat er nu in zit: {description}")
        print("Type de naam van de kamer waar je naartoe wilt gaan:")
        print(opties)
        nextRoom = input()
        os.system("clear")
      else:
        #GEEFT AAN WAAR JE BENT
        print(f"Je bent hier: {title}")
        print(description)
        print("Type de naam van de kamer waar je naartoe wilt gaan:")
        #TOONT ALLE MOGELIJKE LOCATIES
        print(opties)
        nextRoom = input()
        os.system("clear")
        #INVENTORY
        if nextRoom.lower() == "c" and "glas" not in inventory:
          table = [['Er staat hier een glas, wil je die oppakken? (j/n)']]
          print(tabulate(table, tablefmt='grid'))
          oppakken = input()
          if oppakken.lower().strip() == 'j':
            inventory.append("glas")
            print('Het item zit nu in je inventory')
            print("Type de naam van de kamer waar je naartoe wilt gaan:")
            print(opties)
            nextRoom = input()
            os.system("clear")
            game(nextRoom)
          else:
            print("Oke, type dan maar de naam van de kamer waar je naartoe wilt gaan:")
            print(opties)
            nextRoom = input()
            game(nextRoom)
            os.system("clear")
        #INPUT CONTROL
        #currentlocatie[opties] doet t nog niet!!
        elif nextRoom.lower().strip() not in locatie:
          print("Sorry, dit is niet een geldige ruimte, probeer opnieuw")
          print("Type de naam van de kamer waar je naartoe wilt gaan:")
          print(opties)
          nextRoom = input()
          game(nextRoom)
        else:
          #NAAR DE VOLGENDE RUIMTE
          game(nextRoom)
    #DE GAME START BIJ DE BAR
    game("a")
        
  elif antwoord.lower().strip() == "n":
    antwoord = input("De manager had dit niet verwacht. Hij had je als een behulpzaam persoon ingeschat, maar dit valt hem zeer tegen. Je bent nooit meer welkom in zijn restaurant. Een maand later zie je in de krant dat het restaurant failliet is. [GAME O]").lower().input()
  else: 
    print(f"{antwoord} is niet een geldige optie, {naam}. Probeer opnieuw") 
    antwoord = input()