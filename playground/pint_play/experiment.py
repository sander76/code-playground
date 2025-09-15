from pint import Quantity, UnitRegistry

ureg = UnitRegistry()

q1 = Quantity(10, "m/s")
print(q1)

q2 = Quantity(20, "km/h")

print(q2)

print(q1 + q2)


meters = Quantity(10, "m")
seconds = Quantity(2, "s")

print(meters / seconds)
