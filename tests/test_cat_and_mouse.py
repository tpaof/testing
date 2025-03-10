from production_code.cat_and_mouse import cat_and_mouse
import unittest

class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        x, y, z = 2, 5, 3
        expected = "Cat A"

        result = cat_and_mouse(x, y, z)

        self.assertEqual(result, expected)

    def test_cat_b_wins(self):
        x, y, z = 2, 5, 6
        expected = "Cat B"

        result = cat_and_mouse(x, y, z)

        self.assertEqual(result, expected)

    def test_mouse_escapes(self):
        x, y, z = 1, 3, 2
        expected = "Mouse C"

        result = cat_and_mouse(x, y, z)

        self.assertEqual(result, expected)

    def test_out_of_range_low(self):
        x, y, z = 0, 5, 4

        with self.assertRaises(ValueError):
            cat_and_mouse(x, y, z)

    def test_out_of_range_high(self):
        x, y, z = 2, 101, 4

        with self.assertRaises(ValueError):
            cat_and_mouse(x, y, z)

    def test_equal_distances_mouse_escapes(self):
        x, y, z = 4, 6, 5
        expected = "Mouse C"
        result = cat_and_mouse(x, y, z)
        self.assertEqual(result, expected)