# GCD and LCM Calculator
# Calculates the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two numbers.

# Finds the Greatest Common Divisor (GCD) of two numbers using recursion.
def get_gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return get_gcd(a - b, b) # Euclidean algorithm: gcd(a, b) = gcd(a-b, b)
    return get_gcd(a, b - a) # Euclidean algorithm: gcd(a, b) = gcd(a, b-a)

# Finds the Least Common Multiple (LCM) of two numbers.
def get_lcm(a, b):
    # LCM(a, b) * GCD(a, b) = |a * b|
    # So, LCM(a, b) = (|a * b|) / GCD(a, b)
    if a == 0 or b == 0:
        return 0 # The LCM of any number with 0 is 0.
    common_divisor = get_gcd(a, b)
    return abs(a * b) // common_divisor 

try:
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    calculated_gcd = get_gcd(first_num, second_num)
    print(f'GCD of {first_num} and {second_num} is {calculated_gcd}')
    calculated_lcm = get_lcm(first_num, second_num)
    print(f'LCM of {first_num} and {second_num} is {calculated_lcm}')
except ValueError:
    print("Invalid input. Please enter whole numbers only.")