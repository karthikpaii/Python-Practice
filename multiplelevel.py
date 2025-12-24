class grandparent:
    def funct(self):
        print("Hello GrandFather")
    
class parent(grandparent):
    def funct1(self):
        print("Hello Parent")

class child(parent):
    def funct3(self):
        print("Hello Child")

test=child()
test.funct()
test.funct1()
test.funct3()