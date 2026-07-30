#Print your name 10 times without loop
def name(n):
    
    namer = input("Enter your name")
    if n==0:
        print("Done")
        return 
    else:
      print(namer)
      name(n-1)
name(10)
