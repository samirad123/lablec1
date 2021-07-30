a = int(input("Enter number of row: "))
b = int(input("Enter number of coloumn: "))
matrix = []
for i  in range(a):
    c = []
    for j in range(b):
        j = int(input("Enter 1st matrix number: "))
        c.append(j)
    matrix.append(c)
matrix1 = []
for i in range(a):
    d = []
    for j in range(b):
        j = int(input("Enter 2nd matrix number: "))
        d.append(j)
    matrix1.append(d)

print("1st Matrix: ")
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end = "  ")
    print()
print("2nd Matrix: ")
for i in range(b):
    for j in range(b):
        print(matrix1[i][j],end = "  ")
    print()
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(a):
    for j in range(b):
        result[i][j] = matrix[i][j] * matrix1[i][j]

print("Result matrix: ")
for i in range(a):
    for j in range(b):
        print(result[i][j],end = "  ")
    print()



