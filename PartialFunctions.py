#Partial Functions are similar to default arguments
import functools
def add(n1,n2,n3):
    return n1+n2+n3
a = functools.partial(add,5,4)
print(a(4))
