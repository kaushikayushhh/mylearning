def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result


# Calling the function with a sample number
num = 5
output = factorial(num)

print("Factorial of", num, "is:", output)