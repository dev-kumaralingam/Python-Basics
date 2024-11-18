def oddeven(i):
        if(i%2==0):
            return False
        
        return True
        
        
l=list(map(int,input("Enter a value: ").split()))
for i in l:
    if(oddeven(i)):
         print(i)
    else:
         pass


        