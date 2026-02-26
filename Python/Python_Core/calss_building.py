class building:
    no_of_rooms=3
    total_buildings=0
    def __init__(self,name,wifi):
        self.name=name
        self.wifi=wifi
        building.total_buildings+=1
b1=building("xyz",1)
print(b1.name)
print(b1.wifi)
print(b1.total_buildings)
print(building.no_of_rooms)
b2=building("vaishu's_palace",2)
print(b2.name)
print(b2.wifi)
print(b2.total_buildings)

