class house():
    """описание дома"""
    def __init__(self, street, number):
        """properties home"""
        self.street = street
        self.number = number
        self.age = 0
    def build(self):
        """build house"""
        print("Home on street " + self.street + " number "+ str(self.number) + " built")
    def age_of_house(self,year):
        """age home"""
        self.age+=year

house1=house('gghxfh',2320)
house2=house('xbbxhx', 45)

print(house1.number)

house1.build()
print(house1.age)
house1.age_of_house(5)
print(house1.age)


class prospecthouse(house):
    """prospect houses"""
    def __int__(self, prospect, number):
        super().__init__(self,number)
        self.prospect = prospect
prhouse = prospecthouse('ngsfbsbfd', 78)
print(prhouse.number)