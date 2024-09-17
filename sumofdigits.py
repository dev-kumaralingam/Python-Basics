def sumofdigits(n):
    sum=0
    while(1):
        a=n%10
        n=n//10
        sum=sum+a
        if n==0:
            break
    print("Sum:",sum)

n=int(input("Enter a value: "))
sumofdigits(n)