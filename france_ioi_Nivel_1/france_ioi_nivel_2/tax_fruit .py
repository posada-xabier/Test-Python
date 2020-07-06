from math import * 
tax = float(input())
new_tax = float(input())
total_prix = float(input())

prix_ht = total_prix / (1 + tax/100 )

new_total_prix = round(prix_ht * ( 1+ new_tax/100), 2)

print(new_total_prix)