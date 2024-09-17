def cointask(n1,n2):
    p=[]
    n=[]
    c=[]
    for i in n2:
        if (i>0):
            p.append(i)
        else:
            n.append(i)
    p=sorted(p,reverse=True)
    n=sorted(n)
    
    l1=len(p)
    l2=len(n)
    if(l1>l2):
        l1=l1-l2
        for i in range(l1):
            n.append(0)


    else:
        l2=l2-l1
        for i in range(l2):
            n.append(0)
    l1=len(p)
    l2=len(n)
    
    sum=0
   
    f=l1+l2
    for i in range(f//2):
        ind=p[i]
        c.append(ind)
        ind=n[i]
        c.append(ind)

    
    count=c.count(0)
    for i in range(count):
        c.remove(0)

    print(c)
    k=len(c)
    for i in range(0,k,1):
        if(i%2==0):
          sum+=c[i]
        else:
            sum-=c[i]
    print(sum)  
       
        


n1=int(input("Enter a number of coins: "))
n2=list(map(int,input("Enter a value coins: ").split()))
cointask(n1,n2)