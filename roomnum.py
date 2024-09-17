def roomnum(a,b,c):
   l=len(a)
   if(l==c):
     print(l-b)
   else:
      print("Enter correct details")

a=list(map(int,input("Enter a reserved Room no's: ").split()))
b=int(input("Enter a count of Reserved Rooms: "))
c=int(input("Enter a Total number of Rooms: "))
roomnum(a,b,c)