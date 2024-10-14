n=int(input("Enter a value(number of values): "))
a=0
b=1
print(a,b,end=" ")
for i in range(n-1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    