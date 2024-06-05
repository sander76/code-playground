import pickle


class CorrectError(Exception):
    def __init__(self, message: str, context: dict) -> None:
        self.context = context
        super().__init__(message, context)


class IncorrectError(Exception):
    def __init__(self, message: str, context: dict) -> None:
        super().__init__(message)  # notice the absence of the context dict.
        self.context = context

    def __str__(self):
        return f"incorrect error with message {self!r} and {self.context}"


class CapturingError(Exception): ...


context_dict = {"my_key": "my_value"}

_incorrect = IncorrectError("mymessage", context=context_dict)
_correct = CorrectError("mymessage", context=context_dict)


def go():
    try:
        raise IncorrectError("some stuff", context={"mycontext": 10})
    except Exception as err:
        _captured = CapturingError(str(err))
        raise _captured


def pickle_depickle(exception):
    _pickled = pickle.dumps(exception)
    _de_pickled = pickle.loads(_pickled)
    return _de_pickled


print("\n\npickling correct exception.")
print(pickle_depickle(_correct))

try:
    go()
except CapturingError as err:
    print("\n\npickling _capturing exception.")
    print(pickle_depickle(err))

# print("\n\npickling incorrect exception.")
# print(pickle_depickle(_incorrect))
