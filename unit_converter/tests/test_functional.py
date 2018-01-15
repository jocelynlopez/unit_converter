#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

from decimal import Decimal as D

import pytest

from unit_converter.converter import convert

TESTS_CASES = [
    # (quantity, expected_value, desired_unit)

    # Simple units
    ('52 °C', D('325.15'), 'K'),
    ('52 °C', D('52'), '°C'),
    ('52 °C', D('125.6'), '°F'),
    ('1545 m', D('1.545'), 'km'),
    ('1.5 mm', D('1.5E3'), 'µm'),
    ('72 kg', D('72E6'), 'mg'),

    # Composed units
    ('1.5 N*m', D('1.5E3'), 'N*mm'),
    ('1.5 N*m', D('1.5'), 'kN*mm'),
    ('315.2 daN*mm', D('3.152'), 'N*m'),
    ('178mm^2', D('0.000178'), 'm^2'),
    ('120MPa*m^0.5', D('3794.733192202055198398672254'), 'MPa*mm^0.5'),
]

TESTS_TOLERANCE_FALSE = [
    # (quantity, expected_value, desired_unit)
    ('1 m', D('1') + D('1E-27'), 'm'),  # Limite fausse de la tolerance
]

TESTS_TOLERANCE_TRUE = [
    # (quantity, expected_value, desired_unit)
    ('1 m', D('1') + D('1E-28'), 'm'),  # Limite vrai de la tolerance
]


@pytest.mark.parametrize("quantity, expected_value, desired_unit", TESTS_CASES)
def test_cases(quantity, expected_value, desired_unit):
    result_value = convert(quantity, desired_unit)
    assert result_value == expected_value


@pytest.mark.parametrize("quantity, expected_value, desired_unit", TESTS_TOLERANCE_TRUE)
def test_cases_tol_true(quantity, expected_value, desired_unit):
    result_value = convert(quantity, desired_unit)
    assert result_value == expected_value


@pytest.mark.parametrize("quantity, expected_value, desired_unit", TESTS_TOLERANCE_FALSE)
def test_cases_tol_false(quantity, expected_value, desired_unit):
    result_value = convert(quantity, desired_unit)
    assert not result_value == expected_value
