"""
Week 14 - activity 2: Create a Decorator to Measure Execution Time
"""

import time

def check_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # records/logs the time before
        result = func(*args, **kwargs) # the function in 'func' gets executed
        end_time = time.time() # records/logs the time after
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

"""Because decorator @check_time is placed on top of time_function(), when
time_function gets called, check_time() gets executed instead
"""
@check_time
def time_function():
    time.sleep(5) # sleeps/pauses for 5 seconds

if __name__ == "__main__":
    time_function() 

'''    
In this example script, decorator is used to add logging of time
to calculate the time taken by time_function() to execute.
The decorator helps in logging to check if time_function() is working as expected.
'''
