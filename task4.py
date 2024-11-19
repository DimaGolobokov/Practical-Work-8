class Nikola:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = f"Я не {name}, а Николай" if name != "Николай" else "Николай"
        self.age = age

person1 = Nikola("Максим", 25)
print(person1.name)
print(person1.age)

try:
    person1.middle_name = "Иванович"
except AttributeError as e:
    print(e)
