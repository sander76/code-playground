class Check:
    def go(self):
        raise ValueError("an error")


class AContextManager:
    def __init__(self) -> None:
        self.check = Check()

    def __enter__(self):
        return self.check

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)


def get_mymanager():
    with AContextManager() as checker:
        yield checker


manager = next(get_mymanager())
manager.go()
