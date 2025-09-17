#OPPGAVE 1, 2, 3, 4, 5 og 6
telefonbok= [] #liste

person1= {"navn": "Kari", "nummer": 71326643}# ordbok med to nøkkler
person2= {"navn": "Ola", "nummer": 34894523}

telefonbok.append(person1)#legger til ordboken i listen
telefonbok.append(person2)

def vis_alle(person):#funskjon kalt vis_alle for å printe ut nøkkler og verdier
    print(f"Navn: {person['navn']} : {person['nummer']}")

for t in telefonbok:#for løkke for å iterere gjennom listen og viser dem en og en
    vis_alle(t)

#OPPGAVE 3
def legg_til():#funksjon for å legge til ny ordbok i listen
    navn= input(f"Skriv navn på personen du vil legge til: ")# input for å legge til person lagret under navn
    nummer= input(f"Skriv nummeret til personen du akkurat skrev navnet på: ")

    person3= {"navn": navn, "nummer": nummer}#lagrer navn og nummer vi fikk som input over under person3
    telefonbok.append(person3)#legger til person3 i ordboken
    print(f"{navn} ble lagt til i telefonboka")#printer bekreftelse på at personen er lagt til

legg_til()#kalle på funksjonen

for t in telefonbok:
    vis_alle(t)

#OPPGAVE 4
def søk():#funksjon
    finn_person = input(f"\n Skriv navnet på personen du vil finne: ")#Lagrer input som variabel
    for person in telefonbok:#for løkke
        if person['navn'].lower() == finn_person.lower(): #if setning 
            print(f"\n {person['navn']} : {person['nummer']}")
            break#avslutte løkken 
    else:#Hvis den ikke fant person i listen, print beskjed
        print(f"Finner ikke personen")

søk()#kalle på funksjonen

# OPPGAVE 5
while True:#while true
     valg = input(f"\n 1. Vis alle \n 2. Legg til ny \n 3. Søk \n 4. Avslutt \n \n")#lagrer input som variabel

     if valg == "1":#hvis input er 1 såkjører den en for løkke som kaller på funksjon
        for t in telefonbok:#for løkke for å skrive ut en person om gangen
            vis_alle(t)

     elif valg == "2":#hvis input er 2 så kaller den på en funksjon
         legg_til()

     elif valg=="3":#hvis input er 3 kaller den på funksjon 
         søk()

     elif valg== "4":
         print(f"Programmet avsluttes")#hvis valg er 4 printes melding og avslutter kode
         break
     else:
         print(f"Det du skrev er ikke gyldig, vennsligst prøv igjen")#hvis ikke printer feilmelding