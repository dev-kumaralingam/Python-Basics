def prime(i):
        if(i<=1):
            return False
        elif(i==2):
            return True
        else:
            for j in range(2,i//2+1):
                if(i%j==0):
                    return False
            return True
        
        
l=list(map(int,input("Enter a value: ").split()))
for i in l:
    if(prime(i)):
         print(i)
    else:
         pass


        