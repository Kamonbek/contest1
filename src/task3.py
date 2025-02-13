import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time
        print(f"{func.__name__} call executed in {execution_time:.4f} sec")
    return wrapper
