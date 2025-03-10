from production_code.two_characters import Two_characters
import unittest


class TestAlternate(unittest.TestCase):
    def test_alternate_mixed_characters(self):
        s = "beabeefeab"
        expected = 5
        self.assertEqual(Two_characters(s), expected)
    
    def test_alternate_all_same_characters(self):
        s = "aaaa"
        expected = 0
        self.assertEqual(Two_characters(s), expected)
    
    def test_alternate_alternating_characters(self):
        s = "abababab"
        expected = 8
        self.assertEqual(Two_characters(s), expected)
    
    def test_alternate_three_repeating_characters(self):
        s = "abcabcabc"
        expected = 6
        self.assertEqual(Two_characters(s), expected)
    
    def test_alternate_single_character(self):
        s = "a"
        expected = 0
        self.assertEqual(Two_characters(s), expected)

    def test_alternate_empty_string(self):
        s = ""
        expected = 0
        self.assertEqual(Two_characters(s), expected)

    def test_alternate_two_different_characters(self):
        s = "abab"
        expected = 4
        self.assertEqual(Two_characters(s), expected)

    def test_alternate_non_alphabetic_characters(self):
        s = "121212"
        expected = 6
        self.assertEqual(Two_characters(s), expected)