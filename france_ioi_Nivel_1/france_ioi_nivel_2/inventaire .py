inventaire = []
for x in range(10):
   inventaire[x] = 0
   
manyMovements = int(input())

for x in range(manyMovements):
   produit =  int(input())
   variation =  int(input())
   inventaire[produit-1] = i nventaire[produit-1] + variation

for y in range(10):
   print(inventaire[y])