# The maze has 22 rows and 12 columns
# create a list: a wannabe nested list
maze = []
# create a row 
row = []
# create a row full of 12 "x"  
for j in range(12):
    row.append(".")

for i in range(22):
    maze.append(row)
# wee can to append lists to a list ang get a nested one

maze[3][11] = "@"

for i in range(20):
    print("")
    for j in range(12):
        print(maze[i][j], end="")


"""
# The maze has 22 rows and 12 columns
# create a list: a wannabe nested list
maze = []
# create a row 
row = []
# create a row full of 12 "x"  
for j in range(12):
    row.append("X")
# testing if the rox has 12 elements :
# print(row) 
# ok ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
# Now I'll try to print with end=""
# print(row, end="")
# whiteline 
# print("")
# The output is exactly the same :
# ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
# lets try something different
#   for j in range(12):
 #       print(row[j], end=" ")
  #  print("")
# Create the nested list
for i in range(22):
    maze.append(row)
# print(maze)

# It works to append lists inside a list, great!
# Now I'll try to do it better, just print the value 
# and just print it to construct the matrix maze

for i in range(20):
    print("")
    for j in range(12):
        print(maze[i][j], end="")
# Great it displays a matrix of dimensions 12*22 
# and all the elements are X. Visually its no good. 
# I'll try later
"""