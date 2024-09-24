def ArmstrongNum(n):
    a=n
    c=0
    while(n>0):
        b=n%10
        c+=b**3
        n=n//10
    if(c==a):
        print(f"{a} is armstrong number")
    else:
        print(f"{a} is not armstrong number")

n=int(input("Enter a value: "))
ArmstrongNum(n)