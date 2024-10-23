arr=list(map(int,input("Enter a value: ").split()))
arr.sort()
mul=arr[len(arr)-1]*arr[0]
print("Mul: ",mul)