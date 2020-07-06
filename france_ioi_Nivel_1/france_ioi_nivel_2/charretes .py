nbCharrettes = int(input())
weight = []
for x in range(nbCharrettes):
    poids = float(input())
    weight.append(poids)
    total = total + poids
average = total / nbCharrettes

for x in range(nbCharrettes):
    incremento = average - weight[x]
    print(incremento)