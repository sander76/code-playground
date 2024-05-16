my_object = [
    {"exception": [{"exc_type": 22}, 2, 3], "name": "sander"},
    {"name": "pipo"},
]

for obj in my_object:
    match obj:
        case {"exception": [{"exc_type": 25}, *other], **rest}:
            print(other)
