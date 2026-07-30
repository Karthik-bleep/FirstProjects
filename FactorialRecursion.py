facto = int(input("Enter a number: "))
def factorial(n):
    fact=1
    if n==0 or n==1:
        print("Factorial is 1")
        return
    else:
      return n *factorial(n-1)

factorial(facto)

