class Animal:
    def __init__(self, name, age):
        self.__name = name  # private variable
        self.__age = age    # private variable
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def sound(self):  # To be overridden by subclasses
        pass