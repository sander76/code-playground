import io

reader = io.BytesIO()
amount = reader.write(b"hello")
reader.flush()

line = reader.readline()
print(line.decode(encoding="utf-8"))
