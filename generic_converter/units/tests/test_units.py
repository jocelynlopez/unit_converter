#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

from decimal import Decimal as D

import pytest

from generic_converter.units.units import Unit, PrefixUnit, UNITS, PREFIXES
from generic_converter.units.parser import GlobalParser, BasicUnitParser


# ------------------------
# Test GlobalParser class
# ------------------------
def test_GlobalParser_get_value():
    string_input = '56.292 kg*m/s^2'
    value_expected = '56.292'
    assert D(value_expected) == GlobalParser().get_value(string_input)


def test_GlobalParser_get_units():
    string_input = '56.292 kg*m/s^2'
    units_expected = 'kg*m/s^2'
    assert units_expected == GlobalParser().get_units(string_input)


# ---------------------------
# Test BasicUnitParser class
# ---------------------------

# Test get_default_unit method
# ----------------------------
def test_BasicUnitParser_get_default_unit():
    string_input = 'aN'
    unit_expected = UNITS['N']
    assert unit_expected == BasicUnitParser().get_default_unit(string_input)


def test_BasicUnitParser_get_default_unit_d_prefix():
    string_input = 'dm'
    unit_expected = UNITS['m']
    assert unit_expected == BasicUnitParser().get_default_unit(string_input)


def test_BasicUnitParser_get_default_unit_da_prefix():
    string_input = 'daN'
    unit_expected = UNITS['N']
    assert unit_expected == BasicUnitParser().get_default_unit(string_input)


def test_BasicUnitParser_get_default_unit_m_prefix():
    string_input = 'mm'
    unit_expected = UNITS['m']
    assert unit_expected == BasicUnitParser().get_default_unit(string_input)

    string_input = 'm'
    unit_expected = UNITS['m']
    assert unit_expected == BasicUnitParser().get_default_unit(string_input)


def test_BasicUnitParser_get_default_unit_T_prefix():
    string_input = 'TN'
    unit_expected = UNITS['N']
    assert unit_expected == BasicUnitParser().get_default_unit(string_input)


# Test get_prefix method
# -----------------------
def test_BasicUnitParser_get_prefix():
    string_input = 'aN'
    prefix_expected = PREFIXES['a']
    assert prefix_expected == BasicUnitParser().get_prefix(string_input)


def test_BasicUnitParser_get_prefix_d_prefix():
    string_input = 'dm'
    prefix_expected = PREFIXES['d']
    assert prefix_expected == BasicUnitParser().get_prefix(string_input)


def test_BasicUnitParser_get_prefix_da_prefix():
    string_input = 'daN'
    prefix_expected = PREFIXES['da']
    assert prefix_expected == BasicUnitParser().get_prefix(string_input)


def test_BasicUnitParser_get_prefix_m_prefix():
    string_input = 'mm'
    prefix_expected = PREFIXES['m']
    assert prefix_expected == BasicUnitParser().get_prefix(string_input)

    string_input = 'm'
    prefix_expected = PREFIXES['']
    assert prefix_expected == BasicUnitParser().get_prefix(string_input)


def test_BasicUnitParser_get_prefix_T_prefix():
    string_input = 'TN'
    prefix_expected = PREFIXES['T']
    assert prefix_expected == BasicUnitParser().get_prefix(string_input)
# -----------------------


def test_BasicUnitParser_get_unit():
    string_input = 'mm'
    unit_expected = Unit('mm', 'millimeter', L=1, coef=D('1E-3'))
    assert unit_expected == BasicUnitParser().get_unit(string_input)
