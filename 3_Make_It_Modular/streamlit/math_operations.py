# Muhammad Yermi Rachman
# J0403231034

def add(x, y):
    """Add two numbers.

    Args:
        x (int): First number.
        y (int): Second number.

    Returns:
        int: Sum of x and y.
        
    >>> add(4, 2)
    6
    >>> add(4, 4)
    8
    """
    return x + y


def subtract(x, y):
    """Subtract two numbers.
    
    Args:
        x (int): First number.
        y (int): Second number.
        
    Returns:
        int: Difference of x and y.
        
    >>> subtract(4, 1)
    3
    >>> subtract(4, 4)
    0
    """
    return x - y


def multiply(x, y):
    """
    This function takes two numbers as input and returns their product.
    
    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.
    
    Returns:
    int or float: The product of x and y.

    >>> multiply(4, 4)
    16
    >>> multiply(4, 0)
    0
    """
    return x * y


def divide(x, y):
    """
    Divide two numbers.
    
    Args:
        x (int): First number.
        y (int): Second number.
        
    Returns:
        float: Quotient of x and y.
        
    >>> divide(4, 4)
    1.0
    >>> divide(4, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Division by zero is not allowed.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

if __name__ == '__main__':
    import doctest
    doctest.testmod()
