#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

import unittest
from decimal import Decimal as D

import pytest
#TODO: Update tests
# from unit_converter.parser import UnitParser
# from unit_converter.units import Unit, UNITS, PREFIXES
# from ..exceptions import UnitDoesntExistError
#
#
# # ------------------------
# # Test UnitParser class
# # ------------------------
# class TestUnitParser(unittest.TestCase):
#
#     # Test _parse_simple_unit method
#     # ----------------------------
#     def test_parse(self):
#         unit_s = 'm^3*s^-2'
#         unit_expected = Unit('', '', L=3, M=0, T=-2, I=0, THETA=0, N=0, J=0,
#                              coef=D('1'), offset=D('0'))
#         self.assertEqual(unit_expected, UnitParser().parse(unit_s))
#
#
# # ------------------------
# # Test GlobalParser class
# # ------------------------
# class TestGlobalParser(unittest.TestCase):
#
#     # Test get_value method
#     # ----------------------------
#     def test_GlobalParser_get_value(self):
#         string_input = '56.292 kg*m*s^-2'
#         value_expected = '56.292'
#         assert D(value_expected) == GlobalParser().get_value(string_input)
#
#     # Test get_units method
#     # ----------------------------
#     def test_GlobalParser_get_units(self):
#         string_input = '56.292 kg*m/s^2'
#         units_expected = 'kg*m/s^2'
#         assert units_expected == GlobalParser().get_units(string_input)
#
#     def test_GlobalParser_get_units_without_space(self):
#         string_input = '56.292kg*m/s^2'
#         units_expected = 'kg*m/s^2'
#         assert units_expected == GlobalParser().get_units(string_input)
#
#     def test_GlobalParser_get_units_BUG_REPORT_1(self):
#         """Test for correction of the current bug :
#         GlobalParser().get_units('178mm^2') == ('178m', 'm^2')
#         """
#         string_input = '178mm^2'
#         units_expected = 'mm^2'
#         assert units_expected == GlobalParser().get_units(string_input)
#
#
# # ---------------------------
# # Test BasicUnitParser class
# # ---------------------------
# class TestBasicUnitParser(unittest.TestCase):
#
#     # Test get_default_unit method
#     # ----------------------------
#     def test_get_default_unit(self):
#         string_input = 'aN'
#         unit_expected = UNITS['N']
#         assert unit_expected == BasicUnitParser().get_default_unit(string_input)
#
#     def test_get_default_unit_d_prefix(self):
#         string_input = 'dm'
#         unit_expected = UNITS['m']
#         assert unit_expected == BasicUnitParser().get_default_unit(string_input)
#
#     def test_get_default_unit_da_prefix(self):
#         string_input = 'daN'
#         unit_expected = UNITS['N']
#         assert unit_expected == BasicUnitParser().get_default_unit(string_input)
#
#     def test_get_default_unit_m_prefix(self):
#         string_input = 'mm'
#         unit_expected = UNITS['m']
#         assert unit_expected == BasicUnitParser().get_default_unit(string_input)
#
#         string_input = 'm'
#         unit_expected = UNITS['m']
#         assert unit_expected == BasicUnitParser().get_default_unit(string_input)
#
#     def test_get_default_unit_T_prefix(self):
#         string_input = 'TN'
#         unit_expected = UNITS['N']
#         assert unit_expected == BasicUnitParser().get_default_unit(string_input)
#
#     def test_get_default_unit_raise_UnitDoesntExistError(self):
#         with pytest.raises(UnitDoesntExistError):
#             BasicUnitParser().get_default_unit('MYUNIT')
#
#     # Test get_prefix method
#     # -----------------------
#     def test_get_prefix(self):
#         string_input = 'aN'
#         prefix_expected = PREFIXES['a']
#         assert prefix_expected == BasicUnitParser().get_prefix(string_input)
#
#     def test_get_prefix_d_prefix(self):
#         string_input = 'dm'
#         prefix_expected = PREFIXES['d']
#         assert prefix_expected == BasicUnitParser().get_prefix(string_input)
#
#     def test_get_prefix_da_prefix(self):
#         string_input = 'daN'
#         prefix_expected = PREFIXES['da']
#         assert prefix_expected == BasicUnitParser().get_prefix(string_input)
#
#     def test_get_prefix_m_prefix(self):
#         string_input = 'mm'
#         prefix_expected = PREFIXES['m']
#         assert prefix_expected == BasicUnitParser().get_prefix(string_input)
#
#         string_input = 'm'
#         prefix_expected = PREFIXES['']
#         assert prefix_expected == BasicUnitParser().get_prefix(string_input)
#
#     def test_get_prefix_T_prefix(self):
#         string_input = 'TN'
#         prefix_expected = PREFIXES['T']
#         assert prefix_expected == BasicUnitParser().get_prefix(string_input)
#
#     # Test get_unit method
#     # ---------------------
#     def test_get_unit(self):
#         string_input = 'mm'
#         unit_expected = Unit('mm', 'millimeter', L=1, coef=D('1E-3'))
#         assert unit_expected == BasicUnitParser().get_unit(string_input)
#
#
# # ------------------------
# # Test ComposedUnitParser class
# # ------------------------
# class TestComposedUnitParser(unittest.TestCase):
#
#     # Test get_units method
#     # ----------------------------
#     def test__get_units(self):
#         composed_unit_as_string = 'kg*m*s^-2'
#         kg = PREFIXES['k'] * UNITS['g']
#         m = UNITS['m']
#         spowerminus2 = Unit('s^-2.0', 'second^-2.0', T=-2)
#         assert ComposedUnitParser()._get_units(composed_unit_as_string) == [kg, m, spowerminus2]
#
#     # Test get_unit method
#     # ----------------------------
#     def test_get_unit(self):
#         composed_unit_as_string = 'kg*m*s^-2'
#         unit_expected = Unit('kg*m*s^-2.0', 'kilogram*meter*second^-2.0', M=1, L=1, T=-2)
#         assert ComposedUnitParser().get_unit(composed_unit_as_string) == unit_expected
