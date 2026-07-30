#Fibonacci Using Recursion
num = int(input("Enter a number: "))
def fib(n):
    if n<=1:
     return n
    else:
      return fib(n-1) +fib(n-2)

for x in range(num):
  print(fib(x))
