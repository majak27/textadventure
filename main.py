import time
import os
from tabulate import tabulate

#dictionary van locaties
locatie = {
  "bar" :  {
    "title" : "bar",
    "description" : "Je kan hier een drankje doen." 
  },
  "gang":{
    "title": "gang",
    "description" :"Je bent bij een kapstok. Handig, want je had je jas nog aan, en met alles op zak zoals je telefoon, portemonnee etc. kan je niet goed werken. Je hangt je jas op. Nu kan je je melden bij de keuken."
  },
  "keuken" : {
    "title": "keuken",
    "description" : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. "
  },
  "bijkeuken": {
    "title" : "bijkeuken",
    "description": "Je kan hier iets doen"
  },
  "opslag": {
    "title": "opslag",
    "description": "locatie5"
  },
  "wc's": {
    "title": "wc's",
    "description": "locatie6"
  },
  "ingang/uitgang": {
    "title": "ingang/uitgang",
    "description": "locatie7"
  },
  "eetgedeelte": {
    "title": "eetgedeelte",
    "description": "locatie8"
  },
  "buitenterras": {
    "title": "buitenterras",
    "description": "locatie9"
  },
  "garage": {
    "title": "garage",
    "description": "locatie10"
  }
}

#inventory list
inventory = []

table = [["Welkom bij het Restaurant Drama!"]]
print(tabulate(table, tablefmt='grid'))
print("Typ 'start' om verder te gaan")
antwoord = input()
os.system('clear')
while True:
#introductie
  if antwoord.lower().strip() == 'start':
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
    print("Je zit aan de bar met een drankje in een restaurant.") 
    time.sleep(1.5)
    print("Het is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.")
    time.sleep(2)
    print("Nog voordat je iets kan zeggen zegt een mannenstem:") 
    print(f"‘Ik betaal het drankje voor beste {naam}  hier!’")
    time.sleep(2)
    print ("Het is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.")
    time.sleep(1.5)
    print("Je moet de manager helpen!" )
    print("Wil jij de manager helpen door middel van het voltooien van taken in en rondom het restaurant? (j/n)")
    antwoord = input()
    os.system('clear')

    #input control
    if antwoord.lower().strip() == "j":
      table = [["De manager is nu al ontzettend tevreden met jou en je spontane hulp.\nHij biedt je zelfs salaris aan als je de taken goed uitvoert. \nJe (eerste) opdracht is een glas water vullen!"]]
      print(tabulate(table, tablefmt='grid'))
      
      #gameloop
      def game(room):
        currentlocatie = locatie[room]

        # get this room's title and description
        title = currentlocatie["title"]
        description = currentlocatie["description"]
          
        # geeft aan waar je bent
        print(f"Je bent hier: {title}")
        print(description)
        print("Type de naam van de kamer waar je naartoe wilt gaan:")
        #toont alle locaties
        print(", ".join(locatie.keys()))
        nextRoom = input()
        os.system("clear")
        #opdracht in de keuken
        if nextRoom == "keuken":
          table = [['Er staat hier een glas, wil je die oppakken? (ja/nee)']]
          print(tabulate(table, tablefmt='grid'))
          oppakken = input()
          if oppakken.lower().strip() == 'ja':
            inventory.append("glas")
            print('het item zit nu in je inventory')
            print("Type de naam van de kamer waar je naartoe wilt gaan:")
            #toont alle locaties
            print(", ".join(locatie.keys()))
            nextRoom = input()

        #input control
        if nextRoom.lower().strip() not in locatie:
            print("Sorry, dit is niet een geldige ruimte, probeer opnieuw")
            nextRoom = input()
            os.system("clear")
          
        else:
          game(nextRoom)

          #naar de volgende ruimte gaan
        game(nextRoom)
        os.system("clear")   
        #start de game bij de bar
      game("bar")
      
    elif antwoord.lower().strip() == "n":
        antwoord = input("De manager had dit niet verwacht. Hij had je als een behulpzaam persoon ingeschat, maar dit valt hem zeer tegen. Je bent nooit meer welkom in zijn restaurant. Een maand later zie je in de krant dat het restaurant failliet is. [GAME O]").lower().input()
    else: 
      print(f"{antwoord} is niet een geldige optie, {naam}. Probeer opnieuw") 
      antwoord = input()

    