class person:
    total_no_phones=0
    def __init__(self,name,age,phone):
        self.name=name
        self.age=age
        self.phone=phone
        if phone:
            person.total_no_phones+=1
print(person.total_no_phones)
p1=person("vaishu",20,False)
print(p1.name)
print(p1.age)
print(person.total_no_phones)

