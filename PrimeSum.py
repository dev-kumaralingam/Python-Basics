def prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n//2+1,1):
            if n%i==0:
                return False
        return True
n=int(input("Enter a range value: "))
sum=0
for i in range(1,n+1,1):
    if prime(i):
        sum+=i
print("Prime Sum: ",sum)