class WithCache:
    def __init__(self):
        self.locals = globals()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc, exc_tb):
        diff_locals = globals().keys() - self.locals.keys()
        print(diff_locals)


def get_mymanager():
    with WithCache():
        a = 1


manager = get_mymanager()
