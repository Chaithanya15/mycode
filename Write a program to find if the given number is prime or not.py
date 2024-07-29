# Write a program to find if the given number is prime or not.

def is_prime_simple(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test the function
number = 29
if is_prime_simple(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
