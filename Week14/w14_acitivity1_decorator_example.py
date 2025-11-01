""" Week 14 Activity 1"""

"""
log_decorator() has a nested 'wrapper' function that calls the function being passed in func.
The wrapper function performs other actions on top of add() function
"""
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

"""
When @log_decorator is placed on top of function add(),
it's equivalent to passing add() to log_decorator()"""
@log_decorator # The '@' is Python's special symbol for decorators
def add(a, b):
    return a + b

if __name__ == '__main__':
    result = add(3, 5)

    """
    1. main function calls add()
    2. because @log_decorator is place on top of the definition of add(), 
    log_decorator is called next.
    3. log_decorator has a wrapper function.
    4. wrapper function performs a print, then calls add(), then performs another print
    5. final result is passed to the original call in main, and gets printed as well.
    """

    print(f"final result = {result}")
