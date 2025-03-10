from production_code.grid_challenge import grid_challenge
import unittest

class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge_sorted_grid(self):
        grid = ["abc", "ade", "efg"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_unsorted_grid(self):
        grid = ["ebc", "ade", "efg"]
        expected = "NO"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_single_row(self):
        grid = ["zxy"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_identical_rows(self):
        grid = ["aaa", "aaa", "aaa"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)
    
    def test_grid_challenge_mixed_case(self):
        grid = ["aBc", "Ade", "eFg"]
        expected = "NO"
        self.assertEqual(grid_challenge(grid), expected)

    def test_single_column(self):
        grid = ["a", "b", "c"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)

    def test_large_grid(self):
        grid = ["a" * 100, "b" * 100, "c" * 100]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)

    def test_non_alphabetic_characters(self):
        grid = ["123", "456", "789"]
        expected = "YES"
        self.assertEqual(grid_challenge(grid), expected)