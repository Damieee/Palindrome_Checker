import unittest
from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal, Panama!"), True)

    def test_invalid_palindrome(self):
        self.assertEqual(is_palindrome("Not a palindrome"), False)

    def test_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

    def test_single_character_string(self):
        self.assertEqual(is_palindrome("a"), True)


if __name__ == '__main__':
    unittest.main()