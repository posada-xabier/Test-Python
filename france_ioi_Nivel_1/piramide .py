pierres = int(input())
haut = 0
blocks = 0
the_end = False
new_haut = 0
new_blocks = 0


while the_end == False:
    new_haut = haut + 1
    new_blocks = blocks + new_haut**2
   
    if new_blocks > pierres:
        
        print(haut)
        print (blocks)
        the_end = True

    elif new_blocks == pierres:
        
        print(new_haut)
        print (new_blocks)
        the_end = True

    else:
        haut = new_haut
        blocks = new_blocks