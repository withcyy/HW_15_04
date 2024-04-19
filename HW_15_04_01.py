class AgeValidatorMeta(type):
    def __new__(cls, name, bases, dct):
        if 'set_age' in dct:
            original_set_age = dct['set_age']
            def new_set_age(self, age):
                if age < 0:
                    raise ValueError("Age cannot be negative")
                original_set_age(self, age)
            dct['set_age'] = new_set_age
        return super().__new__(cls, name, bases, dct)

class Person(metaclass=AgeValidatorMeta):
    def set_age(self, age):
        self.age = age

person = Person()
person.set_age(25)
print(person.age)

