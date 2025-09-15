#OPPGAVE 1, 2, 3, 4, 5 og 6
telefonbok= []

person1= {"navn": "Kari", "nummer": 71326643}
person2= {"navn": "Ola", "nummer": 34894523}

telefonbok.append(person1)
telefonbok.append(person2)

def vis_alle(person):
    print(f"Navn: {person['navn']} : {person['nummer']}")

for t in telefonbok:
    vis_alle(t)


def legg_til():
    navn= input(f"Skriv navn på personen du vil legge til: ")
    nummer= input(f"Skriv nummeret til personen du akkurat skrev navnet på: ")

    person3= {"navn": navn, "nummer": nummer}
    telefonbok.append(person3)
    print(f"{navn} ble lagt til i telefonboka")

legg_til()

