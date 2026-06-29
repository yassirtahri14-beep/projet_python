class Contact :
    def __init__ (self , nom , numero):
        self.nom = nom
        self.numero = numero
    
    def afficher (self):
        print (f"Nom : {self.nom} - Numero : {self.numero}")
contact1 = Contact("yasser","0616287940")
contact1.afficher()
contact2 = Contact("salim","06162746679")
contact2.afficher()
