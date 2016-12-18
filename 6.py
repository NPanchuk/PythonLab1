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
dic = {}
dic[st[0]]=1
print(dic)
for i in range(1,len(st)):
    for key,value in dic.items():
        if st[i]==key:
            value = value+1
            dic[st[i]]=value
            break
        else:
            dic[st[i]]=1
            break
print(dic)