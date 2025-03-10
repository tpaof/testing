from production_code.fizzbuzz import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_3_should_return_Fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(99), "Fizz")

    def test_divisible_by_5_should_return_Buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(100), "Buzz")

    def test_divisible_by_3_and_5_should_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(150), "FizzBuzz")

    def test_not_divisible_by_3_or_5_should_return_not_FizzBuzz(self):
        self.assertEqual(fizzbuzz(7), "not FizzBuzz")
        self.assertEqual(fizzbuzz(11), "not FizzBuzz")
        self.assertEqual(fizzbuzz(101), "not FizzBuzz")

    def test_zero_should_return_FizzBuzz(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")

    def test_negative_numbers(self):
        self.assertEqual(fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz(-5), "Buzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
        self.assertEqual(fizzbuzz(-7), "not FizzBuzz")


