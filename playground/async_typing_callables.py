"""Type checking examples on coroutines.

Doing typechecking with pycharm.
Mypy does seem to be a little more accepting errors here.

Some experimenting according to:

https://github.com/python/typing/issues/424
"""


from typing import Callable, Sequence, Collection, Tuple, Any, Awaitable


async def an_async_function(arg1: str):
    print(arg1)


def non_async(args1: str):
    print(args1)


# Function expecting a callable coroutine.
def a_function(async_function: Callable[..., Awaitable]) -> Awaitable:
    return async_function("hello")


a_function(an_async_function)  # this will work.
a_function(non_async)  # this will give a typing error.


# Function expecting an awaitable.
def function_with_awaitable(awaitable: Awaitable) -> Awaitable:
    return awaitable


function_with_awaitable(an_async_function("hello"))  # this willl work.
function_with_awaitable(an_async_function)  # this will give a typing error.
function_with_awaitable(non_async("hello"))  # this will give a typing error.


# Function expecting multiple callable coroutines.
def function_with_multiple_coroutines(*async_function: Callable[..., Awaitable]):
    return async_function


function_with_multiple_coroutines(
    an_async_function, an_async_function
)  # this will work.
function_with_multiple_coroutines(
    an_async_function, an_async_function()
)  # this will give a typing error.


# Function expecting a callback with specific arguments
async def call_back(arg1, arg2):
    """A callback with arguments."""
    return "call_back"


async def call_back_fail():
    """Failing callback"""
    return "call_back_fail"


def main_function_expecting_callback(c_back: Callable[[object, str], Awaitable[str]]):
    """A function expecting a callback"""
    print(c_back)


main_function_expecting_callback(call_back)
main_function_expecting_callback(call_back_fail)  # this should fail. But does not.
