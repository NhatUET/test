class StringInput(object):
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("nhap chuoi: ")

    def printString(self):
        print(self.s.upper())

strObj = StringInput()
strObj.getString()
strObj.printString()

class Person:
    name = "Person"
    def __init__(self, name = None):
        self.name = name
    
jeffrey = Person("jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

