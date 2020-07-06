
nbProduits = int(input())
nbPersonnes = int(input())
votes = []
results = []

for h in range(nbProduits):
       results[h] = 0

for x in range(nbPersonnes):
    value = int(input())
    for y in range(nbProduits):
        if value == y:
            nbProduits[value] = nbProduits[value] +1
for s in range(nbProduits):
    print (results[s])  

