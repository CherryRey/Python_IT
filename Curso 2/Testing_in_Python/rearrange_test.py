#!/usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_dash(self):
        testcase = "Lope-Vega, Martin"
        expected = "Martin Lope-Vega"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Kennedy, John F."
        expected = "John F. Kennedy"
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()