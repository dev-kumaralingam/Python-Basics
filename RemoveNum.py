str=input("Enter a string: ")
num="0123456789"
res=""
for i in str:
    if i in num:
        pass
    else:
        res+=i
print(res)