nbProduits = int(input())
nbPersonnes = int(input())
votes = []
results = []

for h in range(nbProduits):
   results[h] = 0

for x in range(nbPersonnes):
   prefered = int(input())
   votes.append(prefered)
   
for w in range(nbProduits):   
   for y in votes:
    if y  == w:
       results[w] +=1
for s in range(nbProduits):
    print (results[s])     