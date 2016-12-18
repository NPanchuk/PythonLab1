import random

def maxmin(a):
    min = a[0]
    max = a[0]
    for i in range(0,len(a)):
        if a[i] < min:
            min = a[i]
        if a[i] > max:
            max = a[i]
    b = [max,min]
    return b

a = []
n = int(input("Enter number: "))
for i in range(n):
    x = random.randint(-100,100)
    a.append(x)
print(a)
b = maxmin(a)
print("Max: {0}, min: {1}".format(b[0],b[1]))