import Student
import pickle
n=int(input("How many students: "))
f = open("hilol.txt",'wb')
for x in range(n):
  roll=int(input("Enter roll no: "))
  name = input("Enter name: ")
  obj=Student.studet(roll,name)  
  pickle.dump(obj,f)
