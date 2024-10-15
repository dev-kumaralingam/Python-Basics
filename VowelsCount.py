str1=input("Enter a string: ")
str2="aeiou"
str1=str1.lower()
count=0
for i in str1:
    if i in str2:
        count+=1
print("Number of vowels in the string is: ",count)