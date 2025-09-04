def add(a, b):
    """This function adds two numbers"""
    return a + b

def subtract(a, b):
    """This function subtracts two numbers"""
    return a - b

def multiply(a, b):
    """This function multiplies two numbers"""
    return a * b

def divide(a, b):
    """This function divides two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b