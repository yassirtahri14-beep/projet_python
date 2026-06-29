unite = int(input("en quoi voulez vous convertir les secondes : \n 1 .en minutes \n 2 . en heures" ))
if unite == 1 :
    secondes = int(input("entrez le nombre de secondes : "))
    minutes = float(secondes / 60)
    print("le nombre de minutes est de : " + str(minutes) + " minutes")
elif unite == 2 :
    secondes = int(input("entrez le nombre de secondes : "))
    heures = float(secondes / 3600)
    print("le nombre d'heures est de : " + str(heures) + " heures")
else :
    print("choix invalide !")
