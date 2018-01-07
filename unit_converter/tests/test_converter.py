#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

import unittest
from decimal import Decimal as D

import pytest

from unit_converter.converter import BasicUnitConverter
from unit_converter.units import UNITS
from ..exceptions import UnConsistentUnitsError


# ---------------------------
# Test BasicUnitParser class
# ---------------------------
class Test_BasicUnitConverter(unittest.TestCase):

    # -----------------------------
    # Test get_default_unit method
    # -----------------------------

    # Cases with value as string WITHOUT current_unit:
    # ------------------------------------------------
    def test_convert_value_as_string(self):
        assert D('125.6') == BasicUnitConverter().convert('52', '°F', '°C')

    def test_convert_value_as_string_current_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert('52', '°F', UNITS['°C'])

    def test_convert_value_as_string_desired_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert('52', UNITS['°F'], '°C')

    def test_convert_value_as_string_desired_and_current_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert('52', UNITS['°F'], UNITS['°C'])

    # Cases with value as string WITH current_unit:
    # ---------------------------------------------
    def test_convert_value_as_string_with_unit(self):
        assert D('125.6') == BasicUnitConverter().convert('52 °C', '°F')

    def test_convert_value_as_string_with_unit_desired_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert('52 °C', UNITS['°F'])

    # Cases with value as Decimal:
    # ----------------------------
    def test_convert_value_as_D(self):
        assert D('125.6') == BasicUnitConverter().convert(D('52'), '°F', '°C')

    def test_convert_value_as_D_desired_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert(D('52'), UNITS['°F'], '°C')

    def test_convert_value_as_D_desired_and_current_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert(D('52'), UNITS['°F'], UNITS['°C'])

    def test_convert_value_as_D_current_unit_as_Unit(self):
        assert D('125.6') == BasicUnitConverter().convert(D('52'), '°F', UNITS['°C'])

    # Cases with raising errors:
    # ---------------------------
    def test_convert_assert_wrong_type_desired_unit(self):
        with pytest.raises(TypeError):
            BasicUnitConverter().convert('52', False, '°C')

    def test_convert_assert_wrong_type_current_unit(self):
        with pytest.raises(TypeError):
            BasicUnitConverter().convert('52', '°F', False)

    def test_convert_assert_wrong_type_value(self):
        with pytest.raises(TypeError):
            BasicUnitConverter().convert(False, '°F', '°C')

    def test_convert_assert_UnConsistentUnitsError(self):
        with pytest.raises(UnConsistentUnitsError):
            BasicUnitConverter().convert('52 °C', 'mm')
