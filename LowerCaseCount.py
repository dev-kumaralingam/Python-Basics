str1=input("Enter a value: ")
count=0
for i in str1:
    if(i.islower()):
        count+=1
print("LowerCase charecters count: ",count)