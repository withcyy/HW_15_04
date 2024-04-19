class NameChangerMeta(type):
    def __new__(cls, name, bases, dct):
        if 'name_override' in dct:
            name = dct['name_override']
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=NameChangerMeta):
    pass

class MyRenamedClass(MyClass):
    name_override = "NewClassName"

print(MyClass.__name__)
print(MyRenamedClass.__name__)