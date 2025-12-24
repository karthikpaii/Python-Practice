class parent1:
    def funct1(self):
        print("Hello Dev")

class parent2:
    def funct2(self):
        print("Hello Dev2")

class child(parent1,parent2):
    def funct3(self):
        print("Hello child")

test=child()
test.funct1()
test.funct2()
test.funct3()
