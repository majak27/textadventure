locatie = 'locatie'
title = 'title'
description = 'description'
description2 = 'description2'
description3 = 'description3'
item = 'item'
descriptionItems = 'descriptionItems'
descriptionItems2 = 'descriptionItems2'
lijst = 'lijst'
opties = 'opties'
gameOver = 'gameOver'
nodig = 'nodig'
N = 'n'
O = 'o'
Z = 'z'
W = 'w'

#LOCATIES
locatie = {
  "Bar": {
    title : "Bar",
    description : "Hier kan je een drankje doen, maar om de manager te helpen zal je toch echt eerst moeten gaan werken. (Tip: taken kun je oppakken en vervolgens in je inventory uitgebreid bekijken!)",
    descriptionItems : '1',
    descriptionItems2 : '1',
    opties : "N: Keuken\nO: Gang\nZ: Eetgedeelte\nW: Opslag",
    item : ['bestelling'],
    N: "Keuken",
    O: "Gang",
    Z: "Eetgedeelte",
    W: "Opslag",
    gameOver : 'nee',
    nodig : '',
  }, 
  "Gang":{
    title : "Gang",
    description:"Je bent bij een kapstok. Handig, want je hebt nog al je waardevolle spullen in je jaszak zitten. Je hangt je jas op. Je ziet in je ooghoek een sleutel met het woord 'garage' erop staan. \nZo nu kan je aan het werk!",
    descriptionItems : '1',
    descriptionItems2 : '1',
    opties : "N: Keuken\nO: WC\nZ: Eetgedeelte\nW: Bar",
    item : ["sleutel"],
    N: "Keuken",
    O: "WC",
    Z: "Eetgedeelte",
    W: "Bar",
    gameOver : 'nee',
    nodig : '',
  },
  "Keuken" : {
    title: "Keuken",
    description: "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. We wilden net champignonsoep maken, maar er is geen champignon meer in de voorraadkast van de keuken. Misschien ligt er ergens anders in het restaurant nog een voorraad aan voedsel?",
    description2: "Ah, fijn! Je hebt de champignons gevonden. Laat ze hier maar achter, dan snijden wij ze snel in stukjes om in de pan te doen.\n! De soep wordt meteen geserveerd en valt gelukkig goed in de smaak.",
    descriptionItems : 'champignons',
    descriptionItems2 : '1',
    opties: "N: Bijkeuken\nO: Gang\nZ: Bar\nW: Opslag",
    item : ['champignon taak'],
    N: "Bijkeuken",
    O: "Gang",
    Z: "Bar",
    W: "Opslag",
    gameOver : 'nee',
    nodig : '',
  },
  "Bijkeuken": {
    title : "Bijkeuken",
    description : "Wanneer je alle borden grondig hebt afgewassen komt de manager blij naar je toe met nog een taak voor jou vandaag. Je moet parasols op het buitenterras neerzetten (TIP: de parasols vindt je in de garage!)",
    descriptionItems : '1',
    descriptionItems2 : '1',
    opties : "Z: Keuken",
    item : ['glas water', 'parasol taak'],
    N: "Bijkeuken",
    O: "Bijkeuken",
    Z: "Keuken",
    W: "Bijkeuken",
    gameOver : 'nee',
    nodig : '',
  },
  "Opslag": {
    title: "Opslag",
    description: "Hier is al het voorraad aan eten opgeslagen.",
    description2:"",
    description3:"",
    descriptionItems : '1',
    descriptionItems2 : '1',
    opties : "N: Achteringang\nO: Keuken \nZ: Bar\nW: Garage",
    item : ['champignons'],
    N: "Achteringang",
    O: "Keuken",
    Z: "Bar",
    W: "Garage",
    gameOver : 'nee',
    nodig : '',
  },
  "WC": {
    title : "WC",
    description: "Nou, je moet wel echt nodig... Even rustig op de wc met een boekje... Even je socials checken... Oeps, je bent de tijd vergeten... [game over]",
    descriptionItems : '1',
    descriptionItems2 : '1',
    gameOver: "ja",
  },
  "Ingang": {
    title: "Ingang",
    description: "Niet veel te zien hier..",description2:"Ik neem aan dat je parasols niet voor hier binnen wil gebruiken? Ze zijn toch echt voor buiten bedoeld.",
    descriptionItems : 'parasols',
    descriptionItems2 : '1',
    opties : "N: Eetgedeelte\nO: Buitenterras\n",
    item: [],
    N: "Eetgedeelte",
    O: "Buitenterras",
    Z: "Ingang",
    W: "Ingang", 
    gameOver : 'nee',
    nodig : '',
  },
  "Achteringang" : {
    title: "Achteringang",
    description: "Je denkt dat je zo makkelijk stiekem weg kan gaan? Nou blijf dan maar weg. [GAME OVER]",
    descriptionItems : '1',
    descriptionItems2 : '1',
    gameOver : 'ja',
    nodig : '',
  },
  "Eetgedeelte": {
    title: "Eetgedeelte",
    description: "Oké, je hebt nog niet instructies gekregen, maar zo te zien zijn er obers nodig. Hoe moeilijk kan het nou zijn om mensen hun bestellingen op te nemen? ",
    description2:"Je hebt de bestelling gezien toch? Nou hup hup aan het werk. ",
    description3:"Je hebt het water! Wat heb je dat nou eens goed gedaan! Laat hier maar liggen hoor. De manager is trots.",
    descriptionItems: 'bestelling',
    descriptionItems2: 'glas water',
    opties : "N: Bar\nO: WC \nZ: Ingang\nW: Garage", 
    item: [] ,
    N: "Bar",
    O: "WC",
    Z: "Ingang",
    W: "Garage",
    gameOver : 'nee',
    nodig : '',
  },
  "Buitenterras": {
    title: "Buitenterras",
    description: "Je hebt de parasols nog niet? Je hebt ze wel eerst nodig als je ze wil gebruiken...",
    description2:"Wat ben je weer geweldig! Laat de parasols hier maar achter. Ontzettend bedankt!",
    descriptionItems : 'parasols',
    descriptionItems2 : '1',
    opties:"N: Eetgedeelte\nO: Garage\nW: Ingang",
    item: [],
    N: "Eetgedeelte",
    O: "Garage",
    Z: "Buitenterras",
    W: "Ingang",
    gameOver : 'nee',
    nodig : '',
  },
  "Garage": {
    title: "Garage",
    description: "Ah, mooi je hebt de garagesleutel, want zonder die sleutel kan je natuurlijk niet binnen. Nu kan je bij de berging waar de parasols voor het buitenterras liggen.",
    descriptionItems : '1',
    descriptionItems2 : '1',
    opties : "N: Eetgedeelte \nO: Opslag\nZ: Buitenterras",
    item: ['parasols'],
    N: "Eetgedeelte",
    O: "Opslag",
    Z: "Buitenterras",
    W: "Garage",
    gameOver : 'nee',
    nodig : 'sleutel',
  },
}