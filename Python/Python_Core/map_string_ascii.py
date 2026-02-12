a="vaishu"
def fun(s):
    for i in s:
        return ord(i)
result=list(map(fun,a))
print(result,end="")