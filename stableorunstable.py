def stableorunstable(n):
    a=[]
    d=[]
    c=[]
    count=0
    e=""
    while(1):
        b=n%10
        a.append(b)
        n=n//10
        if (n==0):
            break
    print(a)
    for i in a:
        if i not in d:
            count=a.count(i)
            c.append(count)
            d.append(i)
    l=len(c)
    print(c)
    for j in range(l-1,0-1,-1):
        if(c[j]!=c[0]):
            print("Unstable Number")
            e="Unstable Number"
            break
    if(e!="Unstable Number"):
        print("Stable Number")


            
                

n=int(input("Enter a value: "))
stableorunstable(n)