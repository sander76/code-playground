from furl import furl
from pathlib import Path


# f = furl("http://localhost:/8080").add(path="api/v1")

f = furl("http://localhost:8080/api/v1")


# f.path = "/api/v1/switches"

print(f"{f.url=}")
print(f"{f.origin=}")

f.path = "/__admin"
print(f.url)

f = furl("http://localhost", path=["api", "v"])

print(f.url)

f = furl("")

f = furl("")
f.path = "/api/version/"
(f.path.add("/")).normalize()
another_f = furl(path="/api/version")
another_f.path.add("/")
print(another_f.path == f.path)
print(another_f.path.segments == f.path.segments)
print(f.path)
