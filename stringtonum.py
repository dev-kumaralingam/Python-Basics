def strtonum(n):
    s=""
    for i in n:
        a=ord(i)
        s+=" "+str(a)
    print(s)


def numtostr(m):
    s=""
    i=0
    while(i<len(m)):
            k=int(m[i:i+2])
            if(k>31 and k<100):
                s+=chr(k)
                i+=2
                
            else:
                k=int(m[i:i+3])
                if(k>99 and k<128):
                        s+=chr(k)
                        i+=3
                        
    print(s)
    
n=input("Enter a string to convert ASCII: ")
m=input("Enter a numbers to convert string: ")
strtonum(n)
numtostr(m)
