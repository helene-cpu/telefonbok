#OPPGAVE 1
telefonbok= []

person1= {"navn": "Kari", "nummer": 71326643}
person2= {"navn": "Ola", "nummer": 34894523}

telefonbok.append(person1)
telefonbok.append(person2)

def vis_alle(person):
    print(f"Navn: {person['navn']} : {person['nummer']}")

for t in telefonbok:
    vis_alle(t)