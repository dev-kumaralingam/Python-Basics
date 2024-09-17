n=int(input("Enter a value: "))
bn=format(n,'b')
val=sorted(bn)
s=""
for i in val:
    s+=i
print(int(s,2))

