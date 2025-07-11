#!/usr/bin/env python3
"""
Example demonstrating ExceptionGroup in Python 3.11+
"""

import sys

# Check Python version
if sys.version_info < (3, 11):
    print("This example requires Python 3.11 or higher")
    sys.exit(1)


def function_a():
    """This function raises a ValueError"""
    raise ValueError("Error in function A")


def function_b():
    """This function raises a ValueError with a different message"""
    raise ValueError("Error in function B")


def function_c():
    """This function returns a value"""
    return "A value"


def execute_all_functions():
    """
    Execute all three functions and collect exceptions in an ExceptionGroup
    """
    exceptions = []
    results = {}

    # Try function_a
    try:
        results["A"] = function_a()
    except Exception as e:
        exceptions.append(e)

    # Try function_b
    try:
        results["B"] = function_b()
    except Exception as e:
        exceptions.append(e)

    # Try function_c
    try:
        results["C"] = function_c()
    except Exception as e:
        exceptions.append(e)

    # If we collected any exceptions, raise them as an ExceptionGroup
    if exceptions:
        raise ExceptionGroup("Multiple functions failed", exceptions)

    return results


def main():
    """Main function to demonstrate ExceptionGroup handling"""
    try:
        results = execute_all_functions()
        print("All functions completed successfully!")
        print("Results:", results)
    except ExceptionGroup as eg:
        print(f"Caught an ExceptionGroup with {len(eg.exceptions)} exceptions:")

        # Count how many of each type of exception
        exception_counts = {}
        for i, exc in enumerate(eg.exceptions):
            exc_type = type(exc).__name__
            if exc_type not in exception_counts:
                exception_counts[exc_type] = 0
            exception_counts[exc_type] += 1

            # Print each exception
            print(f"  Exception {i + 1}: {exc_type}: {exc}")

        # Print summary
        print("\nException summary:")
        for exc_type, count in exception_counts.items():
            print(f"  {exc_type}: {count} occurrences")

        # We can still access the successful results
        try:
            print("\nSuccessful results:")
            print(f"  Function C returned: {function_c()}")
        except Exception as e:
            print(f"Unexpected error while accessing function_c: {e}")


if __name__ == "__main__":
    main()
