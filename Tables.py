print("________TABLES PROGRAM___________")
print("Select:- \n1. Multiplication\n2. Addition\n3. Subtraction")
option = int(input("Enter your option:"))
if option > 3:
    print("Invalid Option")
t = int(input("Enter the Table:"))
r = int(input("Enter the Range:"))
if option == 1:
    for i in range(1, r+1):
        print(f"{i} * {t} = {i * t}")
elif option == 2:
    for i in range(1, r+1):
        print(f"{i} + {t} = {i + t}")
elif option == 3:
    for i in range(t, r+t):
        print(f"{i} - {t} = {i - t}")
    