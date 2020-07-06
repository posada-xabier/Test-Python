a1 = int(input())
b1 = int(input())
many_people = int(input())
counter = 0

for person in range(many_people):
    c2 = int(input())
    d2 = int(input())

    if (a1 >= c2 and a1 <= d2) or (b1 >= c2 and b1 <= d2 ) or (c2 >= a1 and c2 >= b1) or (d2 >= a1 and d2 >= b1):
        counter+=1

print(counter)


