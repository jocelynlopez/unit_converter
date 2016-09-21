#!/usr/bin/env python
# coding=utf-8

from common import BaseConverter

M = 'kg'
T = 's'
L = 'm'
THETA = 'K'
I = 'A'
N = 'mol'
J = 'cd'

BASE_UNITS = {
    'g': M * 1E-3,
    's': T,
    'm': L,
    'K': THETA,
    'A': I,
    'mol': N,
    'cd': J,
}

DERIVED_UNITS = {
    'Hz', ('hertz')
}


class PrefixUnit(object):

    PREFIX_SI = {
        'y': {'factor': 1E-24, 'name': 'yocto'},
        'z': {'factor': 1E-21, 'name': 'zepto'},
        'a': {'factor': 1E-18, 'name': 'atto'},
        'f': {'factor': 1E-15, 'name': 'femto'},
        'p': {'factor': 1E-12, 'name': 'pico'},
        'n': {'factor': 1E-9, 'name': 'nano'},
        'µ': {'factor': 1E-6, 'name': 'micro'},
        'm': {'factor': 1E-3, 'name': 'milli'},
        'c': {'factor': 1E-2, 'name': 'centi'},
        'd': {'factor': 1E-1, 'name': 'deci'},
        '': {'factor': 1E0, 'name': ''},
        'da': {'factor': 1E+1, 'name': 'deca'},
        'h': {'factor': 1E+2, 'name': 'hecto'},
        'k': {'factor': 1E+3, 'name': 'kilo'},
        'M': {'factor': 1E+6, 'name': 'mega'},
        'G': {'factor': 1E+9, 'name': 'giga'},
        'T': {'factor': 1E+12, 'name': 'tera'},
        'P': {'factor': 1E+15, 'name': 'peta'},
        'E': {'factor': 1E+18, 'name': 'exa'},
        'Z': {'factor': 1E+21, 'name': 'zetta'},
        'Y': {'factor': 1E+24, 'name': 'yotta'},
    }

    def __init__(self, symbol, name=None, factor=None):
        self.symbol = symbol

        if not name:
            self.name = PREFIX_SI[self.symbol]['name']
        else:
            self.name = name

        if not name:
            self.factor = PREFIX_SI[self.symbol]['factor']
        else:
            self.factor = factor


class Unit(object):

    def __init__(self, symbol, name, M=0, T=0, L=0, THETA=0, I=0, N=0, J=0):
        self.symbol = symbol
        self.name = name

        # Dimensionnal quantities
        self.M = M
        self.T = T
        self.L = L
        self.THETA = THETA
        self.I = I
        self.N = N

    def


m = Unit('m', 'meter', M=1)
g = Unit('g', 'gram', M=1)
m = Unit('m', 'meter', M=1)
m = Unit('m', 'meter', M=1)
m = Unit('m', 'meter', M=1)
m = Unit('m', 'meter', M=1)
m = Unit('m', 'meter', M=1)
m = Unit('m', 'meter', M=1)


VALUE_PATTERN = "[0-9]+.?[0-9]*"
UNIT_PATTERN = "[a-zA-Z]+"
UNIT_REGEX = re.compile("(%s) *(%s)" % (VALUE_PATTERN, UNIT_PATTERN))
result = UNIT_REGEX.match('23.3 m').groups()


class UnitDoesntExist(ValueError):
    pass


class UnitsConverter(BaseConverter):

    def __init__(self, content, desired_unit, current_unit=None):
        self.content = content
        self.current_unit = current_unit
        self.desired_unit = desired_unit

    @staticmethod
    def extract_base_unit(current_unit):
        for unit in UNITS:
            if unit in current_unit:
                return unit
        raise UnitDoesntExist("Unit '%s' doesn't exist !" % current_unit)

    @staticmethod
    def convert_value(value, desired_unit, current_unit, unit):

        coef = PREFIX_SI[prefix]

    @staticmethod
    def convert_string(string)
