#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        # Test an empty list, should return None
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        # Test a list with a single element
        self.assertEqual(max_integer([42]), 42)

    def test_max_at_end(self):
        # Test a list where the max is at the end
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        # Test a list where the max is at the beginning
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_max_in_middle(self):
        # Test a list where the max is in the middle
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_all_equal(self):
        # Test a list where all elements are equal
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_negative_numbers(self):
        # Test a list with all negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        # Test a list with both negative and positive numbers
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_floats(self):
        # Test a list with float values
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        # Test a list with both int and float values
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_large_numbers(self):
        # Test a list with large integer values
        self.assertEqual(max_integer([1000000, 999999, 123456]), 1000000)

if __name__ == '__main__':
    unittest.main()
