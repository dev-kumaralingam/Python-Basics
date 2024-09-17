def series(n):
    i=1
    a=1
    b=2
    c=3
    while (i>0):
        print(a,b,c)
        a=a+1
        b=b+1
        c=c+1
        if i==n:
            break
        i=i+1

n=int(input("Enter a value: "))
series(n)
