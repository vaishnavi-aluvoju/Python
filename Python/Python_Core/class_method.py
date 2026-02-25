class Profile:
    def __init__(self,username):
        self.followers=0
        self.username=username
    def follow(self):
        print("someone started following you")
        self.followers+=1
    def edit(self,a):
        self.username=a
        print("Username changed")
p1=Profile("_mshr_ak")
p1.follow()
print(p1.username)
print(p1.followers)
p1.edit("vaishu_13")
print(p1.username)

