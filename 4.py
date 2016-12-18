def iscont(s,a):
    for i in range(len(a)):
        for j in range(len(s)):
            if a[i]==s[j]:
                return True
    return False
a = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
s = input("Enter string: ")
if(iscont(s,a)):
    print("String contains consonants")
else:
    print("String not contains consonants")