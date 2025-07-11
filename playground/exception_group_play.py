def function_one():
    return 1


raise ExceptionGroup("some message", (function_one(), ValueError("some error")))

for callable in
