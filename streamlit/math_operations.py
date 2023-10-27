def add(x, y):
    return round(x + y, 3)


def subtract(x, y):
    return round(x - y, 3)


def multiply(x, y):
    return round(x * y, 3)


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return round(x / y, 3)
