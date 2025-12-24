class parent:
    def funct(self):
        print("hello parent")

class child1(parent):
    def funct2(self):
        print("hello child1")

class child2(parent):
    def funct3(self):
        print("hello child2")

test1= child1()
test2=child2()

test1.funct()
test1.funct2()
test2.funct3()
