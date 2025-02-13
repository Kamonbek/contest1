import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time before function execution
        func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # End time after execution
        execution_time = end_time - start_time  # Calculate elapsed time
        print(f"{func.__name__} call executed in {execution_time:.4f} sec")
    return wrapper
