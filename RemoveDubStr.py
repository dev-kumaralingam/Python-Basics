str1=input("Enter a value: ")
lis=[]
for i in range(len(str1)):
    lis.append(str1[i])
res1=[]
res=""
for i in lis:
    if i not in res1:
        res+=i
        res1.append(i)
print(res)
