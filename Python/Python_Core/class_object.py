class Books:
    total_Books=0
    def __init__(self,name,Author):
        self.name=name
        self.Author=Author
        Books.total_Books+=1
B1=Books("Life_Lessons","Vaishu")
B2=Books("python","guido")
B3=Books("sister's_Love","sidhu")
print(B1.total_Books)
print(Books.total_Books)
print(B1.name,B1.Author,sep=" by ")
print(B2.name,B2.Author,sep=" by ")
print(B3.name,B3.Author,sep=" by ")
