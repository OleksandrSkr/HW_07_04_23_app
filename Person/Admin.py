from Person.Person import Person

class Admin (Person):
    def __init__(self, name, age,  experience):
        super().__init__(name, age)
        self._experience = experience

    def Registration(self):
        name = input("Enter your name : ")
        age = input("Enter your age : ")
        experience = input ("Enter your experience : ")
        print ("You coped with the task")


    