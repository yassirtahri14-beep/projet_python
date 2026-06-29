contacts = []
for i in range(3):
    nom = input("nom du contact :")
    numero = input ("numero du contact :")
    contact = {"nom":nom, "numero": numero }
    contacts.append(contact)
for contact in contacts:
    print("Nom :", contact["nom"], "- Numéro :", contact["numero"])