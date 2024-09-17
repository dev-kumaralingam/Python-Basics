def missingvalue(a,b):
   l=len(a)
#    c=[]
   if(l<b):
    #  for i in range(a[0],b+1,1):
    for i in range(1,b+1,1):
          if(i not in a):
             a.append(i)
   a=sorted(a)
   print(a)
    

a=list(map(int,input("Enter a value for array: ").split()))
b=int(input("Enter a size of array: "))

missingvalue(a,b)