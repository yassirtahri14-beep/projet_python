with open("C:/Users/user/Desktop/boulot/projet python/gsss.txt","w") as fichier :
    fichier.write("bonjour\n")
    fichier.write("je m'appele yasser\n")
    fichier.write("et j'ai 26 ans \n")
with open("C:/Users/user/Desktop/boulot/projet python/gsss.txt","r") as fichier :
    contenu = fichier.read()
    print(contenu)
with open("C:/Users/user/Desktop/boulot/projet python/gsss.txt","a") as fichier :
    fichier.write("au revoir")
with open("C:/Users/user/Desktop/boulot/projet python/gsss.txt","r") as fichier :
    contenu = fichier.read()
    print(contenu)
