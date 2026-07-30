#UseMapFunction
num =[1,2,3,4,5]
#Goal is to square 
def func(num):
    return num**2
obj = map(func,num)
for c in obj:
    print(c)
