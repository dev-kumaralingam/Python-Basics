def SecondMinimum(arr):
    arr.sort()
    print("Second Minimum: ",arr[1])

arr=list(map(int,input("Enter a values: ").split()))
SecondMinimum(arr)