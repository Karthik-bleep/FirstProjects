import copy
list1 =[1,2,3,4,5]
list2=copy.copy(list1)
print(id(list1[0]))
print(id(list2[0]))
