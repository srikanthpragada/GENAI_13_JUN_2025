import unittest
from isprime import isperfect

class TestIsPerfect(unittest.TestCase):
    def test_perfect_numbers(self):
        # Known perfect numbers
        self.assertTrue(isperfect(6))
        self.assertTrue(isperfect(28))
        self.assertTrue(isperfect(496))
        self.assertTrue(isperfect(8128))

    def test_non_perfect_numbers(self):
        # Numbers that are not perfect
        self.assertFalse(isperfect(1))
        self.assertFalse(isperfect(2))
        self.assertFalse(isperfect(10))
        self.assertFalse(isperfect(12))
        self.assertFalse(isperfect(100))
        self.assertFalse(isperfect(500))

    def test_negative_and_zero(self):
        # Negative numbers and zero should not be perfect
        self.assertFalse(isperfect(0))
        self.assertFalse(isperfect(-6))
        self.assertFalse(isperfect(-28))
        def test_isprime():
            # Test known primes
            assert isprime(2) == True
            assert isprime(3) == True
            assert isprime(5) == True
            assert isprime(7) == True
            assert isprime(11) == True
            assert isprime(13) == True
            assert isprime(17) == True
            assert isprime(19) == True
            assert isprime(23) == True

            # Test known non-primes
            assert isprime(1) == False
            assert isprime(0) == False
            assert isprime(-7) == False
            assert isprime(4) == False
            assert isprime(6) == False
            assert isprime(8) == False
            assert isprime(9) == False
            assert isprime(10) == False
            assert isprime(15) == False
            assert isprime(20) == False

            # Test large prime and non-prime
            assert isprime(97) == True
            assert isprime(100) == False

        # Run the test manually if this file is executed directly
        if __name__ == "__main__":
            test_isprime()
            print("All isprime tests passed.")
if __name__ == "__main__":
    unittest.main()