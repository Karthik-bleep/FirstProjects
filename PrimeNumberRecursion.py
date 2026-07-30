number = int(input("Enter a number: "))
def num(n):
 number=n
 
 if number%(n-1)==0 and n>2:
   print("Composite number")
   return
 else:
     if n==2:
      print("Prime number")
      return
     
 num(n-1)
  
num(number)
