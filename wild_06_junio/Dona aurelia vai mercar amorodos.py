#non vai moi ben, algo fai, fai o parvo canto quere!
# #function
# def punnet():
import random

def definirPrixAndPiece(valeur):
    nbpiece = random.randint(1, 20)
    prix = nbpiece * valeur
    return nbpiece, prix


#var
kgPrice = 5 # /kilos

# How much the stock weight
StrawberryPunnetWeight= round(random.random(),3)

# How punnet in the stock
StrawberryPunnetStock = random.randint(1, 50)

# the price of one punnet
StrawberryPunnetPrice = StrawberryPunnetWeight * kgPrice

# the price of stock
TotalStockPrice = StrawberryPunnetPrice * StrawberryPunnetStock





total = 0
pieces = (0.5, 1, 2)
PocketMoney = [0, 0, 0]

fifty = definirPrixAndPiece(0.5)
PocketMoney[0] = fifty[0]
total = total + fifty[1]
one = definirPrixAndPiece(1)
PocketMoney[1] = one[0]
total = total + one[1]
two = definirPrixAndPiece(2)
PocketMoney[2] = two[0]
total = total + two[1]
nb_strawberrypunnet = total // StrawberryPunnetPrice

if nb_strawberrypunnet >= StrawberryPunnetStock :
    print(StrawberryPunnetStock)
else :
    print(f"Vous pouvez acheter : {nb_strawberrypunnet} barquette/s")
