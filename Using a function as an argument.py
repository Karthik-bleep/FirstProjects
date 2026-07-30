#Using a function as an argument
def add(a,b):
 return a+b
def display(func):
 print(func(10,11))

display(add)
#First we create a function named as add
#then we create another function taking in add
#we call the add function inside display
# then we call the display function outside
