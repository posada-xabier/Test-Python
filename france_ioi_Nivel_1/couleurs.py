many_jetons = int(input("how many jetons? : "))

for jeton in range(many_jetons):
    x =  int(input("x= "))
    y =  int(input("y= "))

    if x < 0 or x > 70 or y < 0 or y > 90:
        couleur = "En dehors de la feuille"
        print("fuera")
    elif ( y < 50 and y > 25)  and  ( x > 20 and x < 45 ):
        couleur = "Dans une zone jaune"
        print("amarillo")
    elif (( y < 45 and y > 15) or (y < 85 and y > 60)) and ( x < 70 and x > 60 ):
        couleur = "Dans une zone rouge"
        print("rojo")
    elif (x>10 and x < 55) and (y < 85 and y > 10):
        couleur = "Dans une zone bleue"
        print("azul")
    
    else:
        couleur = "Dans une zone jaune"
        print("amarillo else")
    print(couleur)