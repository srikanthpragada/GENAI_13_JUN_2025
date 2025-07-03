def isprime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
    

# Test isprime function by calling it with different numbers

if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]
    for number in test_numbers:
        print(f"{number} is prime: {isprime(number)}")


def isperfect(num):
    """Check if a number is perfect."""
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num


def isstrong(num):
    pass 