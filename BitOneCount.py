str1=input("Enter a value: ")
count=0
for i in str1:
    if(i=="1"):
        count+=1
print("One's count: ",count)

print("One's count: ",str1.count("1"))