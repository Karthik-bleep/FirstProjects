#Recursion,Basics
#Recursion is when we call the function inside itself causing it to loop
'''def hello():
    print("Hi")
    hello()'''


#By default recursion limit is set to 1000
#we can change it by using sys module
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
