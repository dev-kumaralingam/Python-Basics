n=int(input("Enter a value: "))
s=str(n)
if(n==0):
    print("0")
elif(n>0):
    n1=s[::-1]
    if(n1[0]=='0'):
        n1=n1.replace('0','',1)
    print(n1)
else:
    n1=abs(n)
    s1=str(n1)
    n1=s1[::-1]
    if(n1[0]=='0'):
        n1=n1.replace('0','',1)
    print("-"+n1)

