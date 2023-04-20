#import Person.Person
#import Person.Admin
#from Person.Person import Person

from Person.Admin import Admin

if __name__ == "__main__":
#    john = Person("john", 23)
#    johns_name = john.get_name()
#    Person.Registration(Person)
    Admin.Registration(Admin)
#    print(__name__)
#    print("hello word")
#    Person.Admin.Registration()
#    print(johns_name)
