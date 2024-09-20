def SecondMaximum(arr):
    arr.sort()
    print("Second Maximum: ",arr[len(arr)-2])

arr=list(map(int,input("Enter a values: ").split()))
SecondMaximum(arr)