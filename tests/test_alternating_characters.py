from production_code.alternating_characters import alternating_characters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_chars(self):
        s = "AAAA"
        expected = 3
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_already_alternating(self):
        s = "ABABABAB"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_mixed_repetitions(self):
        s = "AABABBAA"
        expected = 3
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_length_out_of_range_low(self):
        s = ""
        with self.assertRaises(ValueError):
            alternating_characters(s)

    def test_invalid_characters(self):
        s = "AACB"
        with self.assertRaises(ValueError):
            alternating_characters(s)

    def test_single_character(self):
        s = "A"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_two_same_characters(self):
        s = "AA"
        expected = 1
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_two_different_characters(self):
        s = "AB"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_long_alternating_string(self):
        s = "ABABABABABABABABABAB"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_long_repeated_string(self):
        s = "AAAAAAAAAA"
        expected = 9
        result = alternating_characters(s)
        self.assertEqual(result, expected)

    def test_mixed_case_characters(self):
        s = "AaAaAa"
        with self.assertRaises(ValueError):
            alternating_characters(s)

    def test_non_alphabetic_characters(self):
        s = "A1A1A1"
        with self.assertRaises(ValueError):
            alternating_characters(s)

    def test_whitespace_characters(self):
        s = "A A A"
        with self.assertRaises(ValueError):
            alternating_characters(s)
