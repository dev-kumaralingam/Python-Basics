str1=input("Enter a value: ")
count=0
for i in str1:
    if(i.isupper()):
        count+=1
print("UpperCase charecters count: ",count)