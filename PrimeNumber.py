n = int(input("Enter a number: "))
if n <= 1:
    print("Neither prime nor composite")
else:
    chk = 0
    for i in range(2, (n//2)+1):
        if n % i == 0:
            chk = 1
            break
    if chk == 1:
        print("Not a prime number")
    else:
        print("Prime number")