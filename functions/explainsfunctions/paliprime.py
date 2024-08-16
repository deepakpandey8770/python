# Function to check if a number is prime
def is_prime(n):
    # Prime numbers are greater than 1
    if n > 1:
        # Check divisibility from 2 to half of n
        for i in range(2, n // 2 + 1):
            # If divisible, it's not prime
            if n % i == 0:
                return False
        # If no divisors found, it's prime
        return True
    else:
        return False  # Numbers less than or equal to 1 are not prime

# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        # Extract the last digit
        digit = num % 10
        # Append it to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the number
        num //= 10
    return reversed_num

# Function to check if a number is a palindromic prime
def is_palindromic_prime(n):
    # Reverse the number
    reversed_n = reverse_number(n)
    # Check if it's equal to the original number and if it's prime
    if n == reversed_n and is_prime(n):
        return True
    else:
        return False

# Function to print palindromic prime numbers in a given range
def print_palindromic_primes(lower_limit, upper_limit):
    for num in range(lower_limit, upper_limit + 1):
        # Check if the number is a palindromic prime
        if is_palindromic_prime(num):
            print(num)

# Call the function to print palindromic primes between 1 and 100
print_palindromic_primes(1,1000)
