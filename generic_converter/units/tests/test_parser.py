#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

from decimal import Decimal as D

import unittest
import pytest

from ..units import Unit, UNITS, PREFIXES
from ..parser import GlobalParser, BasicUnitParser
from ..exceptions import UnitDoesntExistError


# ------------------------
# Test GlobalParser class
# ------------------------
class Test_GlobalParser(unittest.TestCase):

    # Test get_value method
    # ----------------------------
    def test_GlobalParser_get_value(self):
        string_input = '56.292 kg*m/s^2'
        value_expected = '56.292'
        assert D(value_expected) == GlobalParser().get_value(string_input)

    # Test get_units method
    # ----------------------------
    def test_GlobalParser_get_units(self):
        string_input = '56.292 kg*m/s^2'
        units_expected = 'kg*m/s^2'
        assert units_expected == GlobalParser().get_units(string_input)


# ---------------------------
# Test BasicUnitParser class
# ---------------------------
class Test_BasicUnitParser(unittest.TestCase):

    # Test get_default_unit method
    # ----------------------------
    def test_get_default_unit(self):
        string_input = 'aN'
        unit_expected = UNITS['N']
        assert unit_expected == BasicUnitParser().get_default_unit(string_input)

    def test_get_default_unit_d_prefix(self):
        string_input = 'dm'
        unit_expected = UNITS['m']
        assert unit_expected == BasicUnitParser().get_default_unit(string_input)

    def test_get_default_unit_da_prefix(self):
        string_input = 'daN'
        unit_expected = UNITS['N']
        assert unit_expected == BasicUnitParser().get_default_unit(string_input)

    def test_get_default_unit_m_prefix(self):
        string_input = 'mm'
        unit_expected = UNITS['m']
        assert unit_expected == BasicUnitParser().get_default_unit(string_input)

        string_input = 'm'
        unit_expected = UNITS['m']
        assert unit_expected == BasicUnitParser().get_default_unit(string_input)

    def test_get_default_unit_T_prefix(self):
        string_input = 'TN'
        unit_expected = UNITS['N']
        assert unit_expected == BasicUnitParser().get_default_unit(string_input)

    def test_get_default_unit_raise_UnitDoesntExistError(self):
        with pytest.raises(UnitDoesntExistError):
            BasicUnitParser().get_default_unit('MYUNIT')

    # Test get_prefix method
    # -----------------------
    def test_get_prefix(self):
        string_input = 'aN'
        prefix_expected = PREFIXES['a']
        assert prefix_expected == BasicUnitParser().get_prefix(string_input)

    def test_get_prefix_d_prefix(self):
        string_input = 'dm'
        prefix_expected = PREFIXES['d']
        assert prefix_expected == BasicUnitParser().get_prefix(string_input)

    def test_get_prefix_da_prefix(self):
        string_input = 'daN'
        prefix_expected = PREFIXES['da']
        assert prefix_expected == BasicUnitParser().get_prefix(string_input)

    def test_get_prefix_m_prefix(self):
        string_input = 'mm'
        prefix_expected = PREFIXES['m']
        assert prefix_expected == BasicUnitParser().get_prefix(string_input)

        string_input = 'm'
        prefix_expected = PREFIXES['']
        assert prefix_expected == BasicUnitParser().get_prefix(string_input)

    def test_get_prefix_T_prefix(self):
        string_input = 'TN'
        prefix_expected = PREFIXES['T']
        assert prefix_expected == BasicUnitParser().get_prefix(string_input)

    # Test get_unit method
    # ---------------------
    def test_get_unit(self):
        string_input = 'mm'
        unit_expected = Unit('mm', 'millimeter', L=1, coef=D('1E-3'))
        assert unit_expected == BasicUnitParser().get_unit(string_input)
