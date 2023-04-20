#import Person.Person
#import Person.Admin
from Person.Person import Person

john = Person("john", 23)
johns_name = john.get_name()

print(johns_name)
from Person.Admin import Admin

if __name__ == "__main__":
    print(__name__)
    print("hello word")
    Person.Admin.Registration()

