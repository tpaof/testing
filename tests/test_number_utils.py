from production_code.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_2_3_5_7__should_return_true(self):
        prime_list = [2, 3, 5, 7, 11, 13]
        result = is_prime_list(prime_list)
        self.assertTrue(result)

    def test_2_3_4_7__should_return_false(self):
        prime_list = [2, 3, 4, 7, 10]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_empty_list__should_return_false(self):
        prime_list = []
        result = is_prime_list(prime_list)
        self.assertTrue(result)  

    def test_single_prime__should_return_true(self):
        prime_list = [17]   
        result = is_prime_list(prime_list)
        self.assertTrue(result)

    def test_single_non_prime__should_return_false(self):
        prime_list = [9]
        result = is_prime_list(prime_list)
        self.assertFalse(result)

    def test_negative_number__should_return_false(self):
        prime_list = [-2, 3, 5]
        result = is_prime_list(prime_list)
        self.assertFalse(result)  

    def test_list_with_one(self):
        prime_list = [1]
        result = is_prime_list(prime_list)
        self.assertFalse(result)  


