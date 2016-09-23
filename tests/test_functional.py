#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

import pytest
import generic_converter.units as u

TESTS_CASES = [
    # (value, current_unit, expected_value, desired_unit)
    (52, u.degreesC, 125.6, u.degreesF),
    (52, u.degreesC, 325.15, 'K'),
    (52, '°C', 52, u.degreesC),
    (52, '°C', 125.6, '°F'),
    (52, '°C', 325.15, 'K'),
    (52, '°C', 52, '°C'),
    (1545, u.m, 1.545, 'km'),
    (1.5, 'mm', 1.5E3, 'µm'),
]


@pytest.mark.parametrize("value, current_unit, expected_value, desired_unit", TESTS_CASES)
def test_cases(value, current_unit, expected_value, desired_unit):
    converter = u.SmartUnitsConverter()
    result_value = converter.convert(value, desired_unit, current_unit)
    assert round(result_value - expected_value, 7) == 0
