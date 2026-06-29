nombre_secret = 89
nombre_propose = int(input("essaie de deviner le nombre secret : "))
while nombre_propose != nombre_secret :
    nombre_propose = int(input("faux , reessaie de deviner le nombre secret : "))
print ("vous avez reussi !!")