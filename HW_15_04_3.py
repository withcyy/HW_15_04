class AttributeAdderMeta(type):
    def __new__(cls, name, bases, dct):
        dct['added_attribute'] = "Attr added"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AttributeAdderMeta):
    pass

print(MyClass.added_attribute)