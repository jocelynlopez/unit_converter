#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

from decimal import Decimal as D

import pytest

from generic_converter.units.parser import GlobalParser


def test_GlobalParser_get_value():
    string_input = '56.292 kg*m/s^2'
    value_expected = '56.292'
    assert D(value_expected) == GlobalParser().get_value(string_input)


def test_GlobalParser_get_units():
    string_input = '56.292 kg*m/s^2'
    units_expected = 'kg*m/s^2'
    assert units_expected == GlobalParser().get_units(string_input)
