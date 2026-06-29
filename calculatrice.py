
operation = int (input("quelle operation voulez vous effectue : \n 1. addition \n 2. soustraction \n 3.multiplication \n 4. division"))
while True :
    try :
        nombre1=float(input("entrez le 1er nombre :"))
        nombre2=float(input("entrez le 2eme nombre :"))
        break
    except ValueError:
        print("erreur:vous avez pas saisi de chiffre ressaie :")
   
    


def addition (a , b):
    return (a+b)
def soustraction (a , b):
    return (a-b)
def multiplication (a , b):
    return (a*b)
def division (a , b):
    return (a/b)
try:
    if operation == 1:
        resultat = addition(nombre1, nombre2)
    elif operation == 2:
        resultat = soustraction(nombre1, nombre2)
    elif operation == 3:
        resultat = multiplication(nombre1, nombre2)
    elif operation == 4:
        resultat = division(nombre1, nombre2)
    print(resultat)
except ZeroDivisionError:
    print("erreur: division par zero impossible")


