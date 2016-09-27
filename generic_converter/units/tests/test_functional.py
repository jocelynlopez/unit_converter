#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

from decimal import Decimal as D

import pytest

import generic_converter.units as u


TESTS_CASES = [
    # (value, current_unit, expected_value, desired_unit)

    # Simple units
    (D('52'), u.degreesC, D('125.6'), u.degreesF),
    (D('52'), u.degreesC, D('325.15'), 'K'),
    (D('52'), '°C', D('52'), u.degreesC),
    (D('52'), '°C', D('125.6'), '°F'),
    ('52', '°C', D('325.15'), 'K'),
    ('52', '°C', D('52'), '°C'),
    ('1545', u.m, D('1.545'), 'km'),
    ('1.5', 'mm', D('1.5E3'), 'µm'),
    ('1.5 mm', None, D('1.5E3'), 'µm'),
    ('52 °C', None, D('52'), '°C'),
    ('52 °C', None, D('125.6'), '°F'),
    ('72kg', None, D('72E6'), 'mg'),

    # Composed units
    ('1.5', 'N*m', D('1.5E3'), 'N*mm'),
    ('1.5', 'N*m', D('1.5'), 'kN*mm'),
    ('315.2', 'daN*mm', D('3.152'), 'N*m'),
    ('178mm^2', None, D('0.000178'), 'm^2'),
    ('120MPa*m^0.5', None, D('3794.733192202055198398672254'), 'MPa*mm^0.5'),
    # ('0.25 mm*°F^-1', None, D('0.9768389318505063'), 'µm*K^-1'),
    # ('10000 °C^2', None, D('139240.9225'), 'K^2'),
]

TESTS_TOLERANCE_FALSE = [
    # (value, current_unit, expected_value, desired_unit)
    ('1', 'm', D('1') + D('1E-27'), 'm'),        # Limite fausse de la tolerance d'egalite
]

TESTS_TOLERANCE_TRUE = [
    # (value, current_unit, expected_value, desired_unit)
    ('1', 'm', D('1') + D('1E-28'), 'm'),        # Limite vrai de la tolerance d'egalite
]


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_CASES)
def test_cases(value, current_unit, expected_value, desired_unit):
    converter = u.SmartUnitsConverter()
    result_value = converter.convert(value, desired_unit, current_unit)
    assert result_value == expected_value


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_TOLERANCE_TRUE)
def test_cases_tol_true(value, current_unit, expected_value, desired_unit):
    test_cases(value, current_unit, expected_value, desired_unit)


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_TOLERANCE_FALSE)
def test_cases_tol_false(value, current_unit, expected_value, desired_unit):
    converter = u.SmartUnitsConverter()
    result_value = converter.convert(value, desired_unit, current_unit)
    assert not result_value == expected_value
