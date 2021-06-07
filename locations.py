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
  "Bar": {
    title : "Bar",
    description : "Hier kan je een drankje doen, maar om de manager te helpen zal je eerst moeten beginnen met je jas ophangen...",
    description2 : 'Je krijgt snel een obersschort toegeworpen en richting de eerste de beste tafel toegestuurd om de bestellingen op te nemen. Maar door alle stress over de soep vergeet je helemaal de bestellingen. Het restaurant krijgt slechte reviews: Slechte obers, bestelling verkeerd opgenomen". [game over]',
    description3: "Ahhh, eindelijk even relaxen na al dat harde werken voor maar 1 gerecht. Je hebt het werken in een restaurant onderschat. Je vraagt de barman om een biertje. Je vergeet even helemaal dat je nog in je werktijd zit. Even later geeft de manger je je laatste taak voor vandaag: parasols uitklappen op het buitenterras (hint: de parasols liggen in de garage).",
    opties : "N: Gang\nO: Keuken\nZ: Ingang",
    item : ['object'],
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
  }, 
  "Gang":{
    title : "Gang",
    description:"Je bent bij een kapstok. Handig, want je hebt nog al je waardevolle spullen in je jaszak zitten. Je hangt je jas op. Je ziet in je ooghoek een sleutel met het woord 'garage' erop staan. \nZo nu kan je aan het werk!",
    description2:"",
    description3:"",
    opties : "N: Keuken\nO: WC\nZ: Eetgedeelte",
    item : ["sleutel"],
    N: "Keuken",
    O: "WC",
    Z: "Eetgedeelte",
  },
  "Keuken" : {
    title: "Keuken",
    description : "Je hebt je jas nog niet opgehangen? Je denkt toch niet met jas aan te kunnen werken? Hang je jas gewoon op joh!",
    description2: "Wat goed dat je er bent. We waren al aan het wachten op onze redder in nood. Je begint met het maken van champignonsoep, maar er is geen champignon meer in de voorraadkast van de keuken. Misschien ligt er ergens anders in het restaurant nog een voorraad aan voedsel?",
    description3: "Ah, fijn! Je hebt de champignons gevonden. Je snijdt ze snel in stukjes en doet ze in de pan en begint de soep te roeren. Na een paar minuten flink geroert te hebben, giet je de soep voorzichtig op de borden. De soep wordt meteen geserveerd en valt gelukkig goed in de smaak. Er moet nu alleen nog worden afgewassen.",
    opties: "N: Bar\nO: Gang\nZ: Ingang",
    item : [],
    N: "Bar",
    O: "Gang",
    Z: "Ingang",
  },
  "Bijkeuken": {
    title : "Bijkeuken",
    description : "Je bent bezig met afwassen. Wanneer je alle borden grondig hebt afgewassen komt de manager blij naar je toe met 1 laatste taak voor jou vandaag. Je moet parasols op het buitenterras neerzetten (een tip: de parasols vindt je in de garage).",
    description2:"",
    description3:"",
    opties : "N: Bar \nO: Keuken\nZ: Garage",
    item : [],
    N: "Bar",
    O: "Keuken",
    Z: "Garage"
  },
  "Opslag": {
    title: "Opslag",
    description: "Hier is al het voorraad aan eten opgeslagen. Je kan hier het benodigde eten of drinken halen. Je hebt je champignons gevonden. Nu kan je verdergaan met je soep.",
    description2:"",
    description3:"",
    opties : "A: Bar\nO: Eetgedeelte \nZ: Keuken",
    item : [],
    N: "Bar",
    O: "Eetgedeelte",
    Z: "Keuken",
  },
  "WC": {
    title : "WC",
    description: "Nou, je moet wel echt nodig... Even rustig op de wc met een boekje... Even je socials checken... Oeps, je bent de tijd vergeten... [game over]",
    description2:"",
    description3:"",
    opties : "",
    item : [],
    N: "",
    O: "",
    Z: ""
  },
  "Ingang": {
    title: "Ingang",
    description: "Je bent nu buiten het restaurant. \nHier is geen kraan of iets om je water te vullen. \nNou ja, je stapt in je auto en rijdt van het restaurant weg... [game over]",
    description2:"Ik neem aan dat je parasols niet voor hier binnen wil gebruiken? Ze zijn toch echt voor buiten bedoeld.",
    description3:"Je weet niet waar de garage is... Nou oké, whatever... Hier 5 euro als dank voor het doen van maar 1 klusje... Je hoeft hietr gelijk niet meer te werken. [game over]",
    opties : "",
    item: [],
    N: "",
    O: ""
  },
  "Eetgedeelte": {
    title: "Eetgedeelte",
    description: "Oké, je hebt nog niet instructies gekregen, maar zo te zien zijn er obers nodig. Hoe moeilijk kan het nou zijn om mensen hun bestellingen op te nemen?",
    description2:"De soep is klaar en iemand moet het serveren... Er is zo te zien een tekort aan obers. Maar hoe moeilijk kan het zijn? Je loopt rechtstreeks naar de tafel die de soep heeft bestelt. ",
    description3:"",
    opties : "N: Bar \nO: Keuken \nZ: Ingang", 
    item: [] ,
    N: "Gang",
    O: "Keuken",
    Z: "Ingang",
  },
  "Buitenterras": {
    title: "Buitenterras",
    description: "Je hebt de parasols nog niet? Je hebt ze wel eerst nodig als je ze wil gebruiken...",
    description2:"",
    description3:"",
    opties: [],
    item: "",
    N: "Garage",
    Z: "Ingang",
  },
  "Garage": {
    title: "Garage",
    description: "Ah, mooi je hebt de garagesleutel, want zonder die sleutel kan je natuurlijk niet binnen. Nu kan je bij de berging waar de parasols voor het buitenterras liggen.",
    description2:"",
    description3:"",
    opties : "N: Buitenterras \nO: Ingang",
    item: [],
    N: "Buitenterras",
    O: "Ingang",
  },
}