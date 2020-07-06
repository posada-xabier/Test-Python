capital = 0
prix= 0
quantity = 0
while capital <= 0:
    capital = float(input("How much money do you want to spend?  "))
while prix <= 0:
    prix = float(input("Which is the price for one caramel?  "))
while capital >= prix:
    quantity +=1
    capital -= prix

print("You can buy ", quantity, "caramelinhos")