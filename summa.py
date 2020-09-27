from random import random
n = 4
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(random()*20))
    matrix.append(row)
for row in matrix:
    print(row)
asosiy = 0
ikkilamchi = 0
for i in range(n):
    asosiy +=matrix[i][i]
    ikkilamchi += matrix[i][n-i-1]
print("asosiy: ", asosiy)
print("ikkilamchi: ", ikkilamchi)
