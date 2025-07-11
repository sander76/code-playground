class FrozenMeta(type):
    def __new__(cls, name, bases, attrs):
        # Create new FrozenDict for the attributes
        frozen_attrs = dict(attrs)

        # Store original __init__
        original_init = attrs.get("__init__", lambda self: None)

        # Create new __init__ that uses object.__setattr__
        def __init__(self, *args, **kwargs):
            object.__setattr__(self, "_initialized", False)
            original_init(self, *args, **kwargs)
            object.__setattr__(self, "_initialized", True)

        def __setattr__(self, name, value):
            if getattr(self, "_initialized", True):
                raise AttributeError(f"Can't modify frozen class. Attribute '{name}' is read-only")
            object.__setattr__(self, name, value)

        def __delattr__(self, name):
            raise AttributeError(f"Can't modify frozen class. Can't delete attribute '{name}'")

        # Add these methods to the class attributes
        frozen_attrs["__init__"] = __init__
        frozen_attrs["__setattr__"] = __setattr__
        frozen_attrs["__delattr__"] = __delattr__

        return super().__new__(cls, name, bases, frozen_attrs)


class Person(metaclass=FrozenMeta): ...


class Me(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


person = Me(name="myname", age=10)

print(person)
person.name = "another"
