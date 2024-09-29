def Continue(n):
    i=1
    while(i):
        if(i==5):
            continue
        if(i==n):
            break
        print(i)
        i+=1

n=int(input("Enter a value: "))
Continue(n)