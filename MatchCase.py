def MatchCase(n):
    if(n>=3):
        n=3
    match(n):
        case 1:
            print("1")
        case 2:
            print("2")
        case 3:
            print(">=3")

n=int(input("Enter a value: "))
MatchCase(n)