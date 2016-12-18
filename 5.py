def iscontcons(s,a):
    for i in range(len(a)):
        for j in range(len(s)):
            if a[i]==s[j]:
                return True
    return False
def isconthyp(s):
    for i in range(len(s)):
        if s[i]=="-":
            return True
    return False
a = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
r = [ ".", "!", ",","?",":",";"]
s = input("Enter string: ").lower()
for i in range (len(r)):
    s=s.replace(r[i],"")
s=s.split(" ")

str = list()
for i in s:
   if i!="":
        str.append(i)
for i in range(len(str)):
    if iscontcons(str[i],a)==True and isconthyp(str[i])!=True:
        print(str[i])