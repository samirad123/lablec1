m = [ ]
for i in range(2):
    a = []
    for j in range(2):
        j = int(input("Enter number in pocket["+str(i)+"]["+str(j)+"]: "))
        a.append(j)
    m.append(a)
print("Matrix is")

for i in range(2):
    for j in range(2):
        print(m[i][j],end = " ")
    print()
t = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(2):
    for j in range(2):
        t[i][j] = m[j][i]
print("Transpose matrix")
for i in range(2):
    for j in range(2):
        print(t[i][j],end = " ")
    print()