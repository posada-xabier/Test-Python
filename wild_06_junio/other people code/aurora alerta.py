nb_total_mesures = int(input())
temp_min = int(input())
temp_max = int(input())

nb_mesures = 0
temp_mesuree = int(input())

while temp_mesuree <= temp_max and temp_mesuree >= temp_min and nb_mesures != nb_total_mesures :
    temp_mesuree = int(input())
    print("Rien à signaler")
    nb_mesures += 1
         
         

print("Alerte !!")