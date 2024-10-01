def Pass(n):
    i=1
    while(i):
        if(i==5):
            pass
        if(i==n):
            break
        print(i)
        i+=1

n=int(input("Enter a value: "))
Pass(n)