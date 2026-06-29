import random
mot_de_passe = []
for i in range (8):
    chifre= str(random.randint(0, 9))
    mot_de_passe.append(chifre)
mot_de_passe = "".join(mot_de_passe)
print(mot_de_passe)