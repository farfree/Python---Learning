"""
class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __str__ (self):
        return "Name: " + self.name + " Age: " + str(self.age)
    def showName(self):
        print (self.name + " Hello");

alex = person('Alex', 18);
alex.showName()

bob = person('Bob', 30);
bob.showName()

print (alex)

personList = [
                {"name": "Alex", "age":18, "city":"Hisnchu" },
                {"name": "Bob", "age":28, "city":"TT" },
                {"name": "Cat", "age":38, "city":"ZZ" },
                {"name": "Dog", "age":48, "city":"WW" },
            ]

#print (personList[0]["name"])
personList[0]["name"] = "NEWNEW"
#print (personList[0]["name"])
del personList[0]["name"]
#print (personList)

def test(a, b):
    return a+b

test(3,5)
"""
