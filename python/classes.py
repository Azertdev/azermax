class personne:
    def __init__(self, nom, age, profession):
        self.nom = nom
        self.age = age
        self.profession = profession

    def introduction(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans et je suis {self.profession}")


personne1 = personne("Cherif", 19, "en Genie logiciel reseau et systeme")

personne1.introduction()

class vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
            
class voiture(vehicule):
    def klaxonne(self):
        print(f"la marque {self.marque} a comme modele une {self.modele}, et a été creer en {self.annee}")            


class moto(vehicule):
    def klaxonne(self):
        print(f"la marque de moto {self.marque} a comme modele une {self.modele}, et a été creer en {self.annee}")
        

BMW = voiture("BMW", "X8", 2022)
KTM = moto("KTM", "series ninja", 2018)
BMW.klaxonne()
KTM.klaxonne()

class calculatrice():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def soustraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def divisionReel(self):
        if self.b == 0:
            return print("Cannot divide by zero")
        else:
            return self.a / self.b
        
    def reste(self):
        return self.a % self.b

a = calculatrice(5,5)

print(a.addition())
#add une liste de personne si les places sont disponible
class Flyght():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def AddPassenger(self, names):
        count=0
        for name in names:
            count+=1
            if count <= self.capacity:
                print(f"Added {name} to fly succesfully")
                self.passenger.append(name)
            else:
                print(f"No available seats for {name}")

    def PersonAdded(self):
        print(self.passenger)                    



flyght = Flyght(3)
people = ["cherif","lolo","azer","tina","zee","josé"]
flyght.AddPassenger(people)
flyght.PersonAdded()