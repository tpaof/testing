from production_code.guest import guess_float, guess_int
import unittest

class TestRandomGuess(unittest.TestCase):
    def test_guess_int_within_range(self):
        start, stop = 1, 10
        result = guess_int(start, stop)
        self.assertTrue(start <= result <= stop)
        self.assertIsInstance(result, int)

    def test_guess_float_within_range(self):
        start, stop = 1.0, 10.0
        result = guess_float(start, stop)
        self.assertTrue(start <= result <= stop)
        self.assertIsInstance(result, float)

    def test_guess_int_same_start_stop(self):
        start, stop = 5, 5
        result = guess_int(start, stop)
        self.assertEqual(result, 5)

    def test_guess_float_same_start_stop(self):
        start, stop = 7.5, 7.5
        result = guess_float(start, stop)
        self.assertEqual(result, 7.5)

    def test_guess_int_negative_range(self):
        start, stop = -10, -1
        result = guess_int(start, stop)
        self.assertTrue(start <= result <= stop)
        self.assertIsInstance(result, int)

    def test_guess_float_negative_range(self):
        start, stop = -10.0, -1.0
        result = guess_float(start, stop)
        self.assertTrue(start <= result <= stop)
        self.assertIsInstance(result, float)

    def test_guess_int_large_range(self):
        start, stop = 1, 1000000
        result = guess_int(start, stop)
        self.assertTrue(start <= result <= stop)
        self.assertIsInstance(result, int)

    def test_guess_float_large_range(self):
        start, stop = 1.0, 1000000.0
        result = guess_float(start, stop)
        self.assertTrue(start <= result <= stop)
        self.assertIsInstance(result, float)