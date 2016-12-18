import random
import math
n = int(input("Enter number:"))
o = []
for i in range(n):
    x= random.randint(0,50)
    o.append(x)
a =[]
b=[]
for i in range(len(o)):
    if o[i]%2==0:
        a.append(o[i])
    if (math.sqrt(float(o[i])))-int(math.sqrt(float(o[i])))==0:
        b.append(o[i])
print("All numbers: {0}".format(o))
print("A: {0}".format(a))
print("B: {0}".format(b))
print ("Inter: {0}".format(set(a) & set(b)))
print ("Union: {0}".format(set(a) | set(b)))
print ("Sub: {0}".format(set(a) - set(b)))
print ("Diff: {0}".format((set(a) | set(b)) - (set(a) & set(b))))
