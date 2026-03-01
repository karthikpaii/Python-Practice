class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display(self):
        print(f"Make: {self.make} Model:{self.model} Year: {self.year}")


c1=car("Toyota","Aglina",2022)
c1.display()