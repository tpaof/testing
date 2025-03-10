from production_code.stair_case import staircase
import unittest

class TestStaircase(unittest.TestCase):
    def test_staircase_size_4_with_hash(self):
        n = 4
        display = "#"
        expected = "   #\n  ##\n ###\n####"

        result = staircase(n, display)

        self.assertEqual(result, expected)

    def test_staircase_size_1_with_star(self):
        n = 1
        display = "*"
        expected = "*"

        result = staircase(n, display)

        self.assertEqual(result, expected)

    def test_staircase_size_3_with_dollar(self):
        n = 3
        display = "$"
        expected = "  $\n $$\n$$$"

        result = staircase(n, display)

        self.assertEqual(result, expected)

    def test_staircase_invalid_n_below_range(self):
        n = 0
        display = "#"

        with self.assertRaises(ValueError):
            staircase(n, display)

    def test_staircase_invalid_n_above_range(self):
        n = 31
        display = "#"

        with self.assertRaises(ValueError):
            staircase(n, display)

    def test_staircase_large_n(self):
        n = 30
        display = "#"
        expected = "\n".join([" " * (29 - i) + "#" * (i + 1) for i in range(30)])
        result = staircase(n, display)
        self.assertEqual(result, expected)

    def test_staircase_with_special_character(self):
        n = 3
        display = "@"
        expected = "  @\n @@\n@@@"
        result = staircase(n, display)
        self.assertEqual(result, expected)
