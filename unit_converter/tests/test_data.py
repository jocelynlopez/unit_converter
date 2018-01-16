#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

import unittest

from unit_converter.data import PREFIXES, UNITS


class TestUnits(unittest.TestCase):

    def test_if_unit_with_prefix_is_unique(self):
        complete_units = []
        complete_units_debug = []
        for prefix in PREFIXES:
            for unit in UNITS:
                c_unit = prefix + unit
                if c_unit in complete_units:
                    complete_units_debug.append(prefix + "." + unit)
                complete_units.append(c_unit)

        assert len(complete_units_debug) == 0

