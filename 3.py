import random
def summatr(a, b, n1):
    c = []
    for i in range(int(n1[0])):
        v = []
        for k in range(int(n1[1])):
            x = a[i][k]+b[i][k]
            v.append(x)
        c.append(v)
    return c
def mulmatr(a,b,n1,n2):
    c = []
    for i in range(int(n1[0])):
        v = []
        for j in range(int(n2[1])):
            x=0
            for k in range(int(n1[1])):
                x += a[i][k] * b[k][j]
            v.append(x)
        c.append(v)
    return c
n1 = input("Enter size matrix a: ").split(" ")
n2 = input("Enter size matrix b: ").split(" ")
a = []
b = []
for i in range(int(n1[0])):
    c = []
    for k in range(int(n1[1])):
        x=random.randint(-100,100)
        c.append(x)
    a.append(c)
for i in range(int(n2[0])):
    c = []
    for k in range(int(n2[1])):
        x=random.randint(-100,100)
        c.append(x)
    b.append(c)

print("a: {0}".format(a))
print("b: {0}".format(b))
if int(n1[0])!=int(n2[0]) or int(n1[1])!=int(n2[1]):
    print("Матрицы разного размера!")
else:
    print("a+b: {}".format(summatr(a, b, n1)))
if int(n1[1])==int(n2[0]):
    print("a*b: {}".format(mulmatr(a, b, n1,n2)))
else:
    print("Умножение невохможно!")

