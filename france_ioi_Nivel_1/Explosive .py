nb_mesures = int(input())
little = int(input())
bigger = int(input())


for mesure in range(nb_mesures):
    x  = int(input())
    
    if x >= little and x <= bigger:
        print("Rien à signaler")

    if x < little or x > bigger:
        print("Alerte !!")



