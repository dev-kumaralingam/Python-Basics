arr1=list(map(int,input("Enter a value: ").split()))
arr2=list(map(int,input("Enter a value: ").split()))
if(len(arr1)<len(arr2)):
    print(arr1)
else:
    print(arr2)