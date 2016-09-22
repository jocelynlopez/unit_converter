#!/usr/bin/env python
# coding=utf-8

import re

from common import BaseConverter


# Exceptions :
# ------------
class UnitDoesntExist(ValueError):
    pass


class UnconsistentUnits(ValueError):
    pass

# Units classes :
# ---------------


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

    def __init__(self, symbol, name, L=0, M=0, T=0, I=0, THETA=0, N=0, J=0, coef=1., offset=0.):
        self.symbol = symbol
        self.name = name
        self.coef = coef
        self.offset = offset

        # Dimensionnal quantities
        # -----------------------
        self.L = L              # Length
        self.M = M              # Mass
        self.T = T              # Time
        self.I = I              # Electric current
        self.THETA = THETA      # Thermodynamic temperature
        self.N = N              # Amount of substance
        self.J = J              # Luminous intensity

    def add_prefix(self, prefix):
        self.coef *= prefix.factor

    def is_same_dimension(self, other_unit):
        return (self.L == other_unit.L &
                self.M == other_unit.M &
                self.T == other_unit.T &
                self.I == other_unit.I &
                self.THETA == other_unit.THETA &
                self.N == other_unit.N &
                self.J == other_unit.J)

# Global variables:
# -----------------

# Basic SI units
m = Unit('m', 'meter', L=1)
g = Unit('g', 'gram', M=1, coef=1E-3)
s = Unit('s', 'second', T=1)
A = Unit('A', 'ampere', I=1)
K = Unit('K', 'kelvin', THETA=1)
mol = Unit('mol', 'mole', N=1)
cd = Unit('cd', 'candela', J=1)

# Derived SI units
dC = Unit('°C', 'celsius', THETA=1, offset=273.15)

# # Regex
# VALUE_PATTERN = "[0-9]+.?[0-9]*"
# UNIT_PATTERN = "[a-zA-Z]+"
# UNIT_REGEX = re.compile("(%s) *(%s)" % (VALUE_PATTERN, UNIT_PATTERN))
# # result = UNIT_REGEX.match('23.3 m').groups()


class UnitsParser(object):

    def __init__(unit):
        pass


class BaseUnitsConverter(BaseConverter):

    def __init__(self, content, desired_unit, current_unit=None):
        self.content = content
        self.current_unit = current_unit
        self.desired_unit = desired_unit

    @staticmethod
    def convert_value_with_unit_object(value, desired_unit, current_unit, unit):
        if not current_unit.is_same_dimension(desired_unit):
            raise UnconsistentUnits("Units are not of the same dimension !")
        delta_coef = desired_unit.coef / current_unit.coef
        delta_offset = pass


desired_unit.offset = °C  273.15
current_unit.offset = °K  0

253.15°K - -> -20°C

253.15 - offset
