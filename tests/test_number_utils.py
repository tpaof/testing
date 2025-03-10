from production_code.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_all_prime_numbers(self):
        prime_list = [2, 3, 5, 7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_contains_composite_numbers(self):
        prime_list = [4, 6, 8, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_single_prime_number(self):
        prime_list = [13]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_empty_list(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

if __name__ == "__main__":
    unittest.main()
