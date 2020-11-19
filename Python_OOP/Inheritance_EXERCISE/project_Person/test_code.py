from inheritance_person.child import Child
from inheritance_person.person import Person

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
print(Person.__mro__)
print(Child.__mro__)