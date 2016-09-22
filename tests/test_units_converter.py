#!/usr/bin/env python
# -*- encoding=utf-8 -*-

import unittest
from generic_converter.units import UnitsConverter


VALUE_TESTS_CASES = {
    'meter': [
        {'content': 1, 'desired_unit': 'mm'}
    ]
}


class TestUnitsConverter(unittest.TestCase):

    def test_meters(self):
        pass

if __name__ == '__main__':
    unittest.main()
