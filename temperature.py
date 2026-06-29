unite =int (input("choisissez quelle unite de mesure de temperature vous voulez convertir : \n 1. Celsius \n 2. Fahrenheit "))
if unite == 1 :
    celsius = float(input("entrez la temperature en Celsius : "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"la temperature en Fahrenheit est de :  {fahrenheit}  °F")
elif unite == 2 :
    fahrenheit = float(input("entrez la temperature en Fahrenheit : "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"la temperature en Celsius est de :   {celsius}   °C")
else :
    print("choix invalide !")