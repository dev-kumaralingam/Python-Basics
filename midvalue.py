def midvalue(n):
   b=[]
   k=[]
   for i in n:
      if i>0:
         k.append(i)

    
   b=sorted(k)
   print(b)
   l=len(b)
   e=l//2

   if(l==0):
      print("None")
   elif(l%2==0):
      c=b[e]+b[e-1]
      d=c/2
      print(d)
   else:
      f=b[e]
      print(f)


n=list(map(int,input("Enter a value: ").split()))
midvalue(n)

