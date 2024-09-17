def maximum(a,b,c):
    sum=0
    if(a>=c) and (b>=c):
        sum=b+a
    if(b>=a) and (c>=a):
        sum=c+b
    if(a>=b) and (c>=b):
        sum=a+c
    print(sum)

a=int(input("Enter a value1: "))
b=int(input("Enter a value2: "))
c=int(input("Enter a value3: "))
maximum(a,b,c)