#!/usr/bin/env python
# coding=utf-8

import unittest
from units import UnitsConverter


VALUE_TESTS_CASES = {
    'meter': [
        {'content': 1, 'desired_unit': 'mm'}
    ]
}


class TestUnitsConverter(unittest.TestCase):

    def test_meters(self):


if __name__ == '__main__':
    unittest.main()
