def go():
    for i in range(10):
        yield i


def do_stuff(generator):
    first_item = next(generator)

    print(f"first item: {first_item}")

    for i in generator:
        print(i)


do_stuff(go())
