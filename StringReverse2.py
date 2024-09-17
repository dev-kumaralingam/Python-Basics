def StringReverse2(n):
    # for i in range(len(n)-1,0,-1):
    #     print(n[i],end=" ")
    b=' '.join(n.split()[::-1])
    print(b)
n=input("Enter a String: ")
StringReverse2(n)