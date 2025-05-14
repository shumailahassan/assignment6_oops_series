#16. Function Decorators: Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().


def decorator_func(original_func):
    def wrapper():
        print("Function is being called")  # extra kaam
        original_func()  # function call
    return wrapper

@decorator_func
def say_hello():
    print("Hello!")

say_hello()
