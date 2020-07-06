row_1 = [1,2,3]
row_2 = [4,5,6]
row_3 = [7,8,9]
matrix = [row_1, row_2 ,row_3]
print(matrix)

x,y = 3,2

position_row = y-1
position_column = x-1

matrix[position_row][position_column] = "@"
# fila 2 columna 1 son index, it means i=3 j= 2
print(matrix)