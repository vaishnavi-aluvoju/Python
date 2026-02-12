from functools import reduce
def fun(a,b):
    return a+b
l=['P', 'y', 't', 'h', 'o', 'n']
l1=reduce(fun,l)
print(l1)