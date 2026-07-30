#Calling Function Inside a Function
def kar():
    print("My name is karthik")
    def swa():
        print("My name is swaminathan")
    return swa #passing fucntion as a object

d =kar() #will return the object of function
d()
#kar() gets the object location of swa() function, inorder to execute print we call
