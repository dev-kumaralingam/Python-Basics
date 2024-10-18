str1=input("Enter a value: ")
count=0
for i in str1:
    if(i=="0"):
        count+=1
print("Zeros count: ",count)

print("Zeros count: ",str1.count("0"))