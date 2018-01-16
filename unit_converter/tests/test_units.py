#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

import unittest
from decimal import Decimal as D

import pytest

#TODO: Update tests

#
# # ---------------------------
# # Test BasicUnitParser class
# # ---------------------------
# class TestUnitPrefix(unittest.TestCase):
#
#     # -----------------------------
#     # Test __init__ method
#     # -----------------------------
#     def test___init__factor_as_int(self):
#         with pytest.raises(TypeError):
#             UnitPrefix('mp', 'my_prefix', 1)
#
#     def test___init__factor_as_float(self):
#         with pytest.raises(TypeError):
#             UnitPrefix('mp', 'my_prefix', 1.0)
#
#     def test___init__factor_as_D(self):
#         assert D('1') == UnitPrefix('mp', 'my_prefix', D('1.0')).factor
#
#     def test___init__factor_as_string(self):
#         assert D('1') == UnitPrefix('mp', 'my_prefix', '1.0').factor
#
#     # -----------------------------
#     # Test is_same_factor method
#     # -----------------------------
#     def test_is_same_factor(self):
#         compared_prefix = UnitPrefix('mp2', 'my_prefix2', D('02.4500000'))
#         assert UnitPrefix('mp', 'my_prefix', '2.45').is_same_factor(compared_prefix)
#
#     # -----------------------------
#     # Test __mult__ method
#     # -----------------------------
#     def test___mult__(self):
#         expected_unit = Unit('µm', 'micrometer', L=1, coef=D('1E-6'))
#         assert UnitPrefix('µ', 'micro', D('1.0E-6')) * UNITS['m'] == expected_unit
#
#     def test___mult__raise_TypeError(self):
#         with pytest.raises(TypeError):
#             UnitPrefix('µ', 'micro', D('1.0E-6')) * False
#
#
# # ---------------------------
# # Test Unit class
# # ---------------------------
# class TestUnit(unittest.TestCase):
#
#     # -----------------------------
#     # Test __mult__ method
#     # -----------------------------
#     def test___mult__(self):
#         assert UNITS['N'] * UNITS['m'] == Unit('N*m', 'newton*meter', M=1, L=2, T=-2)
#         assert UNITS['°C'] * UNITS['m'] == Unit('°C*m', 'celsius*meter', L=1, THETA=1, offset=D('273.15'))
#
#     def test___mult__raise_TypeError(self):
#         with pytest.raises(TypeError):
#             UNITS['°C'] * False
#
#     # -----------------------------
#     # Test __pow__ method
#     # -----------------------------
#     def test___pow__(self):
#         assert UNITS['m'] ** 3 == Unit('m^3', 'meter^3', L=3)
#
#     def test___pow___coef(self):
#         mm = Unit('mm', 'millimeter', L=1, coef=D('1E-3'))
#         assert mm ** 3 == Unit('mm^3', 'millimeter^3', L=3, coef=D('1E-9'))
#
#     # def test___pow___offset(self):
#     #     assert UNITS['mm'] ** 3 == Unit('mm^3', 'millimeter^3', L=3, coef=D('1E-9'))
#
#     def test___pow__raise_TypeError(self):
#         with pytest.raises(TypeError):
#             UNITS['m'] ** '3'
