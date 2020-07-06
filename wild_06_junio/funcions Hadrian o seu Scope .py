def nomTest(pikachu, nom):
    return pikachu + " " + nom

def prenomTest(chaine, prenom):
    return chaine + " " + prenom
    
def nomPrenomCapitaliz(prenom, nom):
    prenom = prenom.capitalize()
    nom = nom.capitalize()
    return prenom, nom
    
prenom = str(input("quel est ton prenom : "))
nom = str(input("quel est ton nom : "))

chaine = "Je m'apelle"
chaineA = chaine + " " + nom

chaineA = chaineA + " " + prenom

print("Classic Way")
print(chaineA)

maj = nomPrenomCapitaliz(prenom, nom)
nom = maj[1]
prenom = maj[0]

chaineB = nomTest(chaine, nom)
chaineB = prenomTest(chaineB, prenom)

print("function Way")
print(chaineB)