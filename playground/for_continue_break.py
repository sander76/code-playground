def demo_continue():
    for i in range(10):
        # print(i)
        if i == 3:
            print(f"hit nr {i}")
            continue  # skip all code below and go for the next item in the loop.
        print(i)


demo_continue()
