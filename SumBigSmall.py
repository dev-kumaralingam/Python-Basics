arr=list(map(int,input("Enter a value: ").split()))
arr.sort()
sum=arr[0]+arr[len(arr)-1]
print("Sum: ",sum)