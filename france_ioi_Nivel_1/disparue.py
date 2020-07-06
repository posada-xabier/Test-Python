ci_x = int(input())
how_many = int(input())
sorti = 0

for x in range(how_many):
    ci_signed = int(input())
    if ci_signed == ci_x and sorti == 0:
        print("Sorti de la ville")
        sorti = 1
if sorti == 0:
    print("Encore dans la ville")