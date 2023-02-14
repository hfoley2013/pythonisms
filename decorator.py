import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

# Using the decorator to time a function
@time_it
def slow_function():
    time.sleep(2)

if __name__ == '__main__':
    slow_function()
    
