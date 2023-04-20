class Person :
    def __init__ (self, name, age):
        self._name = name
        self._age = age

    def Registration(self):
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        print("oops")
        print(self._name, self._age)
        

    def get_name(self):
        return self._name

