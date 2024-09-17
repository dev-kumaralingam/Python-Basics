def StringReverse1(n):
    for i in range(len(n)-1,0-1,-1):
        print(n[i],end="")

n=input("Enter a String: ")
StringReverse1(n)