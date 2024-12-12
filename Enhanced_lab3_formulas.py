import math

# Existing basic operations
def add(values):
    """Add a list of numbers."""
    return sum(values)

def subtract(values):
    """Subtract a list of numbers, starting with the first."""
    if not values:
        return 0
    total = values[0]
    for x in values[1:]:
        total -= x
    return total

def multiply(values):
    """Multiply a list of numbers."""
    if not values:
        return 0
    total = values[0]
    for x in values[1:]:
        total *= x
    return total

def divide(values):
    """Divide the first number by subsequent numbers in the list."""
    if not values or len(values) == 1:
        return values[0] if values else 0
    total = values[0]
    for x in values[1:]:
        if x == 0:
            raise ValueError("Cannot divide by 0")
        total /= x
    return total

# Trigonometric functions
def calculate_sin(angle_radians):
    """Calculate the sine of an angle (in radians)."""
    return math.sin(angle_radians)

def calculate_cos(angle_radians):
    """Calculate the cosine of an angle (in radians)."""
    return math.cos(angle_radians)

def calculate_tan(angle_radians):
    """Calculate the tangent of an angle (in radians)."""
    return math.tan(angle_radians)

# Add functions to calculate the area of shapes (for completeness)
def calculate_square_area(side):
    """Calculate the area of a square."""
    return side ** 2

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)
