arr=list(map(int,input("Enter a value: ").split()))
arr.sort()
sub=arr[len(arr)-1]-arr[0]
print("Sub: ",sub)