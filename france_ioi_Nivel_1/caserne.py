nb_pairs=int(input())

for pair in range(nb_pairs):

   ax=int(input())
   bx=int(input())
   
   ay=int(input())
   by=int(input())
   
   cx=int(input())
   dx=int(input())   
  
   cy=int(input())
   dy=int(input())
   
   
   
   
   if (( cx > ax and cx < bx ) or ( dx > ax and dx < bx ) or ( ax > cx and ax < dx ) or ( bx > cx and bx < dx )) and (( cy > ay and cy < by ) or ( dy > ay and dy < by ) or ( ay > cy and ay < dy ) or ( by > cy and by < dy )):
      
      print("OUI")
   else:
      print("NON")
      
      
   
   