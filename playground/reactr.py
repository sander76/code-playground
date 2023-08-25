from asyncio import Event
from collections import defaultdict
import gc
from weakref import WeakMethod


class Reactr:
    def __init__(self, default) -> None:
        self._default = default

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type) -> object:
        return obj.__dict__.get(self.name) or self._default

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value
        obj.publish(self.name, value)


class ReactrModel:
    def get_weakref(self, func):
        return WeakMethod(func, self.unsubscribe)

    def __init__(self) -> None:
        self._subscriptions = defaultdict(list)
        self._weakrefs = {}

    def publish(self, property: str, value):
        for subscription in self._subscriptions[property]:
            subscription()(value)

    def subscribe(self, property, callback):
        weakref = self.get_weakref(callback)
        self._subscriptions[property].append(weakref)
        if weakref in self._weakrefs:
            raise Exception("Alread an identical weakref available.")
        self._weakrefs[weakref] = property

    def unsubscribe(self, weakref, *args, **kwargs):
        prop = self._weakrefs[weakref]
        subscriptions = self._subscriptions[prop]
        subscriptions.remove(weakref)
        print("removed")


class Values(ReactrModel):
    value1 = Reactr(10)
    value2 = Reactr(12)


values = Values()


class Controller:
    def __init__(self, values: Values) -> None:
        self._values = values
        values.subscribe(Values.value1, self._update_value1)
        values.subscribe("value2", self._update_value_2)

    def _update_value1(self, value):
        print(f"update value1 {value}")

    def _update_value_2(self, value):
        print(f"update value2 {value}")


controller = Controller(values)
values.value1 = 10
values.value2 = 28
# refs = gc.get_referrers(controlle1)
# print(len(refs))
del controller
gc.collect()


values.value1 = 12
values.value2 = 33
