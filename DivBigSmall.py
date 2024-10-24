arr=list(map(int,input("Enter a value: ").split()))
arr.sort()
div=arr[len(arr)-1]/arr[0]
print("Div: ",div)