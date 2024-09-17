def bin2decimal():
    n=int(input("Enter a binary value for bin2decimal: "))
    val=str(n)
    print("bin2decimal: ",int(val,2))

def bin2octal():
    n=input("Enter a binary value for bin2octal: ")
    
    print("bin2octal: ",format(n,'o'))

def bin2hexadecimal():
    n=int(input("Enter a binary value for bin2hexadecimal: "))
    val=str(n)
    h=int(val,2)
    print("bin2hexadecimal: ",format(h,'x'))

def decimal2bin():
    n=int(input("Enter a decimal value for decimal2bin: "))
    print("decimal2bin: ",format(n,'b'))

def decimal2octal():
    n=int(input("Enter a decimal value for decimal2octal: "))
    print("decimal2octal: ",format(n,'o'))

def decimal2hexadecimal():
    n=int(input("Enter a decimal value for decimal2hexadecimal: "))
    print("decimal2hexadecimal: ",format(n,'x'))

def octal2bin():
    n=int(input("Enter a octal value for octal2bin: "))
    print("octal2bin: ",format(n,'b'))

def octal2decimal():
    n=int(input("Enter a octal value for octal2decimal: "))
    val=format(n,'b')
    s=""
    for i in val:
        s+=i
    print("octal2decimal: ",int(s,2))

def octal2hexadecimal():
    n=int(input("Enter a octal value for octal2hexadecimal: "))
    val=format(n,'b')
    s=""
    for i in val:
        s+=i
    h=int(s,2)
    print("octal2hexadecimal: ",format(h,'x'))

def hexadecimal2bin():
    n=input("Enter a hexadecimal value for hexadecimal2bin: ")
    print("hexadecimal2bin: ",format(n,'b'))

def hexadecimal2octal():
    n=input("Enter a hexadecimal value for hexadecimal2octal: ")
    print("hexadecimal2octal: ",format(n,'o'))

def hexadecimal2decimal():
    n=input("Enter a hexadecimal value for hexadecimal2decimal: ")
    print("hexadecimal2decimal: ",int(n,2))

def main():
    while(True):
        print("1. Binary to Decimal")
        print("2. Binary to Octal")
        print("3. Binary to Hexadecimal")
        print("4. Octal to Binary")
        print("5. Octal to Decimal")
        print("6. Octal to Hexadecimal")
        print("7. Hexadecimal to Binary")
        print("8. Hexadecimal to Octal")
        print("9. Hexadecimal to Decimal")
        print("10. Exit")
      
        ch=int(input("Enter your choice: "))
        if(ch==10):
            break

        match(ch):
            case 1:
                bin2decimal()
                
            case 2:
                bin2octal()
                
            case 3:
                bin2hexadecimal()
                
            case 4:
                octal2bin()
                
            case 5:
                octal2decimal()
                
            case 6:
                octal2hexadecimal()
                
            case 7:
                hexadecimal2bin()
                
            case 8:
                hexadecimal2octal()
                
            case 9:
                hexadecimal2decimal()
            

main()
    