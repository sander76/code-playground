class MyClass:
    def __init__(self):
        self.values = []

    def add(self, value: int):
        """Add a value.

        Args:
            value: some value.

        Returns:
            list of values.

        Examples:
            >>> my_class.add(10)
            [11]
        """
        self.values.append(value)
        return self.values
