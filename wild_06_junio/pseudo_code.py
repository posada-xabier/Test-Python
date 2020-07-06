argent = float(input("tela marinera? :"))
prix =  float(input("precio unitario? :"))

bonbon = 0

while argent > 0 :
    if (argent - prix)>=0:
        argent = argent - prix
        bonbon+=1
    else:
        print("no tengo dinero")
print("llevate " ,bonbon)