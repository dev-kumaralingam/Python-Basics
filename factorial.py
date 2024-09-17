n = int(input("Enter a Number:"))
f = 1
if n < 0:
    pass
else:
    for i in range(2, n+1):
        f = f * i
    print(f"Factorial of {n} is {f}")