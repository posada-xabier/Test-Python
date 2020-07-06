alfaNumber = int(input())

if alfaNumber >= 0:
    zone = alfaNumber % 24

if alfaNumber < 0:
    alfaNumber = alfaNumber * (-1)
    zone = 24 - alfaNumber % 24

print(zone)