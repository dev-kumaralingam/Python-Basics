from collections import Counter
def repeat(n):
    a=0
    b=[]
    c=[]
    count=0
    while(1):
        a=n%10
        b.append(a)
        n=n//10
        if(n==0):
            break
    print(b)
    for i in b:
       if i not in c: 
          a=b.count(i)
          if a>1:
            print(i)
            # print("count",a)
            c.append(i)

    d=Counter(b)
    
    print(d)       

n=int(input("Enter a value: "))
repeat(n)
        