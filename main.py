#dictionary van locaties
locatie = {
  "bar" :  {
    "title" : "bar",
    "description" : "Je kan hier een drankje doen." 
  },
  "kapstok":{
    "title": "kapstok",
    "description" :"Je bent bij een kapstok. Handig, want je had je jas nog aan, en met alles op zak zoals je telefoon, portemonnee etc. kan je niet goed werken. Je hangt je jas op. Nu kan je je melden bij de keuken."
  },
  "keuken" : {
    "title": "keuken",
    "description" : "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. "
  },
  "kantoor": {
    "title" : "kantoor",
    "description": "Je kan hier iets doen"
  },
  "locatie5": {
    "title": "locatie5",
    "description": "locatie5"
  },
  "locatie6": {
    "title": "locatie6",
    "description": "locatie6"
  },
  "locatie7": {
    "title": "locatie7",
    "description": "locatie7"
  },
  "locatie8": {
    "title": "locatie8",
    "description": "locatie8"
  },
  "locatie9": {
    "title": "locatie9",
    "description": "locatie9"
  },
  "locatie10": {
    "title": "locatie5",
    "description": "locatie10"
  }
}

#dictionary van objecten
objecten = {
  "object1":{
    "title": "object1",
    "description":"description"
  },
  "object2":{
    "title": "object2",
    "description":"description"
  },
}

#introductie
print("Restaurant spel")
naam = input("Wat is je naam? ")
print(f"Hallo {naam}, welkom bij het spel!")
print("Je zit aan de bar met een drankje in een restaurant.")
print("Het is er druk. Je ziet mensen drinken, praten en het gezellig hebben. Je voelt je alleen. Je wil je drankje afrekenen en begint te zoeken naar je portemonnee, maar hij is weg.")
print("Nog voordat je iets kan zeggen zegt een mannenstem:") 
print(f"‘Ik betaal het drankje voor beste {naam} hier!’")
print ("Het is de manager. Hij heeft hulp nodig voor klusjes in en rondom het restaurant. Het restaurant heeft namelijk door de coronacrisis een tekort aan personeel met slechtere opbrengsten als gevolg. Het mag niet failliet gaan, want dit is jouw lievelings restaurant.")
print("Je moet de manager helpen!" )
print( "Wil jij de manager helpen door middel van het voltooien van taken in en rondom het restaurant? (ja/nee)")
antwoord = input()

while True:
  #input control
  if antwoord.lower().strip() == "ja":
      print("De manager is nu al ontzettend tevreden met jou en je spontane hulp. Hij biedt je zelfs salaris aan als je de taken goed uitvoert.")
      
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

        #input wordt gecheckt
        if nextRoom.lower().strip() not in locatie:
          print("Sorry, dit is niet een geldige ruimte, probeer opnieuw")
          nextRoom = input()
        else:
          game(nextRoom)

        #naar de volgende ruimte gaan
        game(nextRoom)

      #start de game bij de bar
      game("bar")
      
  elif antwoord.lower().strip() == "nee":
      antwoord = input("De manager had dit niet verwacht. Hij had je als een behulpzaam persoon ingeschat, maar dit valt hem zeer tegen. Je bent nooit meer welkom in zijn restaurant. Een maand later zie je in de krant dat het restaurant failliet is. [GAME O]").lower().input()
    
  else:
    print(f"{antwoord} is niet een geldige optie, {naam}. Probeer opnieuw")
    antwoord = input()