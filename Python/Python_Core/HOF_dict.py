d={"apple": 100, "banana": 40, "cherry": 150}
def fun(a):
    if d[a]>50:
        return True
d1=list(filter(fun,d))
print(d1)