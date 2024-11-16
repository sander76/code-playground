from packaging.version import Version

v = Version("1.0.0.dev1")
v1 = Version("1.0.0")

print(v > v1)
