from pathlib import PurePosixPath

from furl import Path, furl

f = furl("http://localhost:8080").add(path="api/v1")
assert f.url == "http://localhost:8080/api/v1"
f.add(path="names")
assert f.url == "http://localhost:8080/api/v1/names"

f.path = "/__admin"
assert f.url == "http://localhost:8080/__admin"

f = furl("http://localhost", path=["api", "v1"])
assert f.url == "http://localhost/api/v1"


f = furl(path="/api//version")
assert f.url == "/api//version"

f.path.normalize()  # remove the double forward slash
assert f.url == "/api/version"

pth = Path("api/").add("/v1").normalize()
assert str(pth) == "api/v1"

pth = Path(["v1/", "/api/"]).normalize()  # this fails.
# assert str(pth) == "v1/api/"  # this fails.

pth = str(Path("/").add("v1").normalize())
assert pth == "/v1"

pth = Path("v1//api").normalize()
assert str(pth) == "v1/api"


root_path = "/root/"
docs_url = "/static/swagger-ui-bundle.js"

print(str(furl(root_path) / docs_url))
