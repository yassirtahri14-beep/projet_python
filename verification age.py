verification_carte = input ("avez vous une carte de membres :")
age = int (input("quelle est votre age :"))
if age >= 18 and verification_carte == "oui":
    print ("acces autorise!")
elif age >= 18 and verification_carte == "non":
    print ("acces refuse : carte membres requise !")
elif age < 18 :
    print ("acces refuse : vous etes trop jeune !")

