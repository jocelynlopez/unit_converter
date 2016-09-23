#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

from decimal import Decimal as D

import pytest

import generic_converter.units as u


TESTS_CASES = [
    # (value, current_unit, expected_value, desired_unit)
    (D('52'), u.degreesC, D('125.6'), u.degreesF),
    (D('52'), u.degreesC, D('325.15'), 'K'),
    (D('52'), '°C', D('52'), u.degreesC),
    (D('52'), '°C', D('125.6'), '°F'),
    ('52', '°C', D('325.15'), 'K'),
    ('52', '°C', D('52'), '°C'),
    ('1545', u.m, D('1.545'), 'km'),
    ('1.5', 'mm', D('1.5E3'), 'µm'),
]

TESTS_TOLERANCE_FALSE = [
    # (value, current_unit, expected_value, desired_unit)
    ('1', 'm', D('1') + D('1E-27'), 'm'),        # Limite de la tolerance d'egalite
]

TESTS_TOLERANCE_TRUE = [
    # (value, current_unit, expected_value, desired_unit)
    ('1', 'm', D('1') + D('1E-28'), 'm'),        # Limite de la tolerance d'egalite
]


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_CASES)
def test_cases(value, current_unit, expected_value, desired_unit):
    converter = u.SmartUnitsConverter()
    result_value = converter.convert(value, desired_unit, current_unit)
    assert (result_value - expected_value) == 0


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_TOLERANCE_TRUE)
def test_cases_tol_true(value, current_unit, expected_value, desired_unit):
    test_cases(value, current_unit, expected_value, desired_unit)


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_TOLERANCE_FALSE)
def test_cases_tol_false(value, current_unit, expected_value, desired_unit):
    converter = u.SmartUnitsConverter()
    result_value = converter.convert(value, desired_unit, current_unit)
    assert not (result_value - expected_value) == 0
