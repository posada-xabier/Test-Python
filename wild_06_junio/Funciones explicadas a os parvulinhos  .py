A = int(input())
print("A = " + str(A))
A = A + 5
B = int(input("Insérer B "))
A = A + B * 2
print("A = " , A)

for C in range (1, 11) :
    A = A + C
    print("A = " + str(A))
    while A > 10 : # while [condition] est vrai.
    
        A = A // 2
    if A % 2 == 0 :
        print("A est pair(" + str(A) + ")")
    else :
        print("A est impair(" + str(A) + ")")

