
'''def sum_num(a,b):
    s=0
    for i in range(a,b+1):
        s+=i
    return s
print(sum_num(1,10))
#print(p)'''
'''def multiple(a,b):
    res=[]
    for i in range(a,b+1):
        if i%4==0:
            res.append(i)
    return res
print(multiple(1,10))'''
'''def multiple(a,b):
    if a>b:
        print("Invalid Range")
    else:
        found=False
        for i in range(a,b+1):
            if i%5==0:
                print(i)
                found=True
    if found==False:
        print("No Numbers")
print(multiple(1,20))'''
def count(a,b):
    c=0
    if a>b:
        print("INVALID RANGE")
    else:
        for i in range(a,b+1):
            if i%2==0:
                c+=1
        if c==0:
            print("NO NUMBERS")
    return c
print(count(23,23))
