import time

def calculate_execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        
        result = func(*args, **kwargs)  
        
        stop_time = time.time()  
        execution_time = stop_time - start_time  
        
        print(f"Execution time for {func.__name__}: {execution_time:.6f} seconds")
        
        return result
    
    return wrapper


