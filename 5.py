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
def spl(s):
    r = [ ".", "!", ",","?",":",";"]
    for i in range (len(r)):
        s=s.replace(r[i],"")
    s=s.split(" ")
    res = list()
    for i in s:
        if i!="":
            res.append(i)
    return res
s = input("Enter string: ").lower()
st = spl(s)
a = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
for i in range(len(st)):
    if iscontcons(st[i],a)==True and isconthyp(st[i])!=True:
        print(st[i])