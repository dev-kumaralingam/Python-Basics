a = list(input("Enter the first string: "))
b = list(input("Enter the second string: "))

a.sort()
b.sort()

if a == b:
    print("Anagram")
else:
    print("Not an Anagram")