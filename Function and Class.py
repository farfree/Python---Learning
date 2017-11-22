
#define function
def sayHi(msg):
    print ("Hello " + msg)

sayHi ("this is sayhi function")

#define class
class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __str__ (self):
        return "Name: " + self.name + " Age: " + str(self.age)
    def showName(self):
        print (self.name + " Hello");

alex = person('Alex', 18);
bob = person('Bob', 30);

print (alex)
alex.showName()
print (bob)
bob.showName()

import bank
acct = bank.Account('Justin', '123-4567', 1000)
acct.deposit(500)
acct.withdraw(200)
print(acct)
