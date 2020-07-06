labirinto = []
row = []
for j in range(10):
    row.append(["x"])
for i in range(20):
    labirinto.append(row)

for i in range(20):
    for j in range(i):
        print(labirinto[i][j], end="")
