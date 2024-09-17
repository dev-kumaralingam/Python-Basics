from multipledispatch import dispatch

class Greatest:
    @dispatch(int, int)
    def greatest_number(self, a, b):
        if a > b:
            return "A is Biggest Number"
        elif b > a:
            return "B is Biggest Number"
        else:
            return "A and B are equal"

    @dispatch(int, int, int)
    def greatest_number(self, a, b, c):
        if a > b and a > c:
            return "A is Biggest Number"
        elif a == b and a > c:
            return "A and B are equal and greater than C"
        elif a == c and a > b:
            return "A and C are equal and greater than B"
        elif b == c and b > a:
            return "B and C are equal and greater than A"
        elif b > c and b > a:
            return "B is Biggest Number"
        elif c > b and c > a:
            return "C is Biggest Number"

    @dispatch(int, int, int, int)
    def greatest_number(self, a, b, c, d):
        if a == b and b == c and a > d:
            return "A, B and C are equal and greater than D"
        elif a == b and b == d and a > c:
            return "A, B and D are equal and greater than C"
        elif d == b and b == c and d > a:
            return "B, C and D are equal and greater than A"
        elif a == d and d == c and a > b:
            return "A, C and D are equal and greater than B"
        elif a == b and a > c and a > d:
            return "A and B are equal and greater than C and D"
        elif a == c and a > b and a > d:
            return "A and C are equal and greater than B and D"
        elif b == c and b > a and b > d:
            return "B and C are equal and greater than A and D"
        elif a == d and a > b and a > c:
            return "A and D are equal and greater than B and C"
        elif b == d and b > a and b > c:
            return "B and D are equal and greater than A and C"
        elif c == d and c > a and c > b:
            return "C and D are equal and greater than A and B"
        elif a > b and a > c and a > d:
            return "A is Biggest Number"
        elif b > c and b > d:
            return "B is Biggest Number"
        elif c > d:
            return "C is Biggest Number"
        else:
            return "D is Biggest Number"


while True:
    try: 
        n = 0
        while n == 0:
            n = int(input("How many numbers do you want to compare(2/3/4):"))
            if n < 2 or n > 4:
                print("Invalid choice!! Try again")
                n = 0
        obj = Greatest
        if n == 4:
            a = int(input("Enter the value of A: "))
            b = int(input("Enter the value of B: "))
            c = int(input("Enter the value of C: "))
            d = int(input("Enter the value of D: "))
            print(obj.greatest_number(a, b, c, d))
            ch = input("Do you want to continue?(y/n)")
            if ch == 'y':
                continue
            else:
                break

        elif n == 3:
            a = int(input("Enter the value of A: "))
            b = int(input("Enter the value of B: "))
            c = int(input("Enter the value of C: "))
            print(obj.greatest_number(a, b, c))
            ch = input("Do you want to continue?(y/n)")
            if ch == 'y':
                continue
            else:
                break

        else:
            a = int(input("Enter the value of A: "))
            b = int(input("Enter the value of B: "))
            print(obj.greatest_number(a, b))
            ch = input("Do you want to continue?(y/n)")
            if ch == 'y':
                continue
            else:
                break
            
    except ValueError:
        print("Invalid input. Give Integers Only")