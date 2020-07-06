many_people = int(input())

for person in range(many_people):

    tall  = int(input())
    age = int(input())
    poids = int(input())
    horse = int(input())
    brun  = int(input())
    suspect_index = 0

    if tall >= 178 and tall <= 182:
        suspect_index +=1
    if age >=35 :
        suspect_index +=1
    if poids < 70:
        suspect_index +=1
    if horse == 0:
        suspect_index +=1
    if brun == 1:
        suspect_index +=1

    if suspect_index == 5:
        print("Tres probable")
    if suspect_index == 4 or suspect_index == 3:
        print("Probable")
    if suspect_index == 2 or suspect_index == 1:
        print("Peu probable")
    if suspect_index == 0:
        print("Imposible")