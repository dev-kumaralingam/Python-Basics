def numtask(n):
   b=[]
   k=[]
   mid=0
   while(1):
      a=n%10
      b.append(a)
      n=n//10
      if n==0:
         break
   l=len(b)
   for i in range(l,0,-1):
      k.append(b[i-1])

   if l%2==0:
      print("Enter a valid input")
   else:
      mid=l//2
      mid=k[mid]

      print(mid)
      pos=k.index(mid)

      if pos==l-1:
         print("once position")
      elif pos==l-2:
         print("ten position")
      elif pos==l-3:
         print(" Hunred position")
      elif pos==l-4:
         print("thousand position")
      elif pos==l-5:
         print("ten thousand position")
      elif pos==l-6:
         print("lakh position") 
      elif pos==l-7:
         print("million position")  
      elif pos==l-8:
         print("ten million position") 
      else:
         print("enter a value below ten million")

n=int(input("Enter a value: "))
numtask(n)

      
   
      

    
  




