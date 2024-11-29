def numstar(num):
    if(num>0):
        print(num*" * ")
    else:
        print("Enter a correct value(num>0)")

num=int(input("Enter a value: "))
numstar(num)