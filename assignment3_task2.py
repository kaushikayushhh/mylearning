import math

# Taking user input
num = float(input("Enter a number: "))

if num < 0:
    print("Square root and logarithm are not defined for negative numbers.")
else:
    # Square root
    square_root = math.sqrt(num)
    
    # Natural logarithm (base e)
    natural_log = math.log(num)
    
    # Sine (input treated as radians)
    sine_value = math.sin(num)

    print("Square Root:", square_root)
    print("Natural Logarithm (log base e):", natural_log)
    print("Sine (in radians):", sine_value)