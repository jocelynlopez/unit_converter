#!/usr/bin/env python
# coding=utf-8

from decimal import Decimal as D

# PREFIXES = {
#     'y': {'factor': D('1E-24'), 'name': 'yocto'},
#     'z': {'factor': D('1E-21'), 'name': 'zepto'},
#     'a': {'factor': D('1E-18'), 'name': 'atto'},
#     'f': {'factor': D('1E-15'), 'name': 'femto'},
#     'p': {'factor': D('1E-12'), 'name': 'pico'},
#     'n': {'factor': D('1E-9'), 'name': 'nano'},
#     'µ': {'factor': D('1E-6'), 'name': 'micro'},
#     'm': {'factor': D('1E-3'), 'name': 'milli'},
#     'c': {'factor': D('1E-2'), 'name': 'centi'},
#     'd': {'factor': D('1E-1'), 'name': 'deci'},
#     '': {'factor': D('1E0'), 'name': ''},
#     'da': {'factor': D('1E+1'), 'name': 'deca'},
#     'h': {'factor': D('1E+2'), 'name': 'hecto'},
#     'k': {'factor': D('1E+3'), 'name': 'kilo'},
#     'M': {'factor': D('1E+6'), 'name': 'mega'},
#     'G': {'factor': D('1E+9'), 'name': 'giga'},
#     'T': {'factor': D('1E+12'), 'name': 'tera'},
#     'P': {'factor': D('1E+15'), 'name': 'peta'},
#     'E': {'factor': D('1E+18'), 'name': 'exa'},
#     'Z': {'factor': D('1E+21'), 'name': 'zetta'},
#     'Y': {'factor': D('1E+24'), 'name': 'yotta'},
# }


class PrefixUnit(object):

    def __init__(self, symbol, name, factor):
        self.symbol = symbol
        self.name = name

        if isinstance(factor, str):
            self.factor = D(factor)
        elif isinstance(factor, D):
            self.factor = factor
        else:
            raise TypeError("factor need to be a 'string' or a 'decimal.Decimal' class")

        # if not name:
        #     self.name = PREFIXES[self.symbol]['name']
        # else:
        #     self.name = name

        # if not factor:
        #     self.factor = PREFIXES[self.symbol]['factor']
        # elif isinstance(factor, D) or isinstance(factor, str):
        #     self.factor = D(factor)
        # else:
        #     raise TypeError("factor need to be a 'string' or a 'decimal.Decimal' class")

    def __eq__(self, other_prefix):
        return (self.symbol == other_prefix.symbol and
                self.name == other_prefix.name and
                self.factor == other_prefix.factor)

    def __mul__(self, unit):
        if isinstance(unit, Unit):
            final_unit = Unit(symbol=self.symbol + unit.symbol,
                              name=self.name + unit.name,
                              L=unit.L,
                              M=unit.M,
                              T=unit.T,
                              I=unit.I,
                              THETA=unit.THETA,
                              N=unit.N,
                              J=unit.J,
                              coef=self.factor * unit.coef,
                              offset=unit.offset)
            return final_unit
        else:
            raise TypeError("unsupported operand type(s) for : '%s' and '%s'" % (type(self), type(unit)))


class Unit(object):

    def __init__(self, symbol, name, L=0, M=0, T=0, I=0, THETA=0, N=0, J=0, coef=D('1'), offset=D('0')):
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
        return (self.L == other_unit.L and
                self.M == other_unit.M and
                self.T == other_unit.T and
                self.I == other_unit.I and
                self.THETA == other_unit.THETA and
                self.N == other_unit.N and
                self.J == other_unit.J)

    def __eq__(self, other_unit):
        return (self.is_same_dimension(other_unit) and
                self.symbol == other_unit.symbol and
                self.name == other_unit.name and
                self.coef == other_unit.coef and
                self.offset == other_unit.offset)

    def __mul__(self, unit):
        try:
            final_unit = Unit(symbol=self.symbol + '*' + unit.symbol,
                              name=self.name + '*' + unit.name,
                              L=self.L + unit.L,
                              M=self.M + unit.M,
                              T=self.T + unit.T,
                              I=self.I + unit.I,
                              THETA=self.THETA + unit.THETA,
                              N=self.N + unit.N,
                              J=self.J + unit.J,
                              coef=self.coef * unit.coef,
                              offset=self.offset + unit.offset)
            return final_unit
        except AttributeError:
            raise TypeError("unsupported operand type(s) for : '%s' and '%s'" % (type(self), type(unit)))

    def __pow__(self, power):
        if isinstance(power, int) or isinstance(power, float):
            final_unit = Unit(symbol=self.symbol + '^' + power,
                              name=self.name + '^' + power,
                              L=self.L * power,
                              M=self.M * power,
                              T=self.T * power,
                              I=self.I * power,
                              THETA=self.THETA * power,
                              N=self.N * power,
                              J=self.J * power,
                              coef=self.coef,
                              offset=self.offset)
            return final_unit
        else:
            raise TypeError("unsupported operand type(s) for : '%s' and '%s'" % (type(self), type(unit)))


#-----------
# Prefix SI
# ----------
PREFIXES = {
    'y': PrefixUnit(symbol='y', name='yocto', factor=D('1E-24')),
    'z': PrefixUnit(symbol='z', name='zepto', factor=D('1E-21')),
    'a': PrefixUnit(symbol='a', name='atto', factor=D('1E-18')),
    'f': PrefixUnit(symbol='f', name='femto', factor=D('1E-15')),
    'p': PrefixUnit(symbol='p', name='pico', factor=D('1E-12')),
    'n': PrefixUnit(symbol='n', name='nano', factor=D('1E-9')),
    'µ': PrefixUnit(symbol='µ', name='micro', factor=D('1E-6')),
    'm': PrefixUnit(symbol='m', name='milli', factor=D('1E-3')),
    'c': PrefixUnit(symbol='c', name='centi', factor=D('1E-2')),
    'd': PrefixUnit(symbol='d', name='deci', factor=D('1E-1')),
    '': PrefixUnit(symbol='', name='', factor=D('1E0')),
    'da': PrefixUnit(symbol='da', name='deca', factor=D('1E+1')),
    'h': PrefixUnit(symbol='h', name='hecto', factor=D('1E+2')),
    'k': PrefixUnit(symbol='k', name='kilo', factor=D('1E+3')),
    'M': PrefixUnit(symbol='M', name='mega', factor=D('1E+6')),
    'G': PrefixUnit(symbol='G', name='giga', factor=D('1E+9')),
    'T': PrefixUnit(symbol='T', name='tera', factor=D('1E+12')),
    'P': PrefixUnit(symbol='P', name='peta', factor=D('1E+15')),
    'E': PrefixUnit(symbol='E', name='exa', factor=D('1E+18')),
    'Z': PrefixUnit(symbol='Z', name='zetta', factor=D('1E+21')),
    'Y': PrefixUnit(symbol='Y', name='yotta', factor=D('1E+24')),
}


#----------------
# Basic SI units
# ---------------
m = Unit('m', 'meter', L=1)
g = Unit('g', 'gram', M=1, coef=D('1E-3'))
s = Unit('s', 'second', T=1)
A = Unit('A', 'ampere', I=1)
K = Unit('K', 'kelvin', THETA=1)
mol = Unit('mol', 'mole', N=1)
cd = Unit('cd', 'candela', J=1)


# -----------------
# Derived SI units
# -----------------
Hz = Unit('Hz', 'hertz', T=-1)
N = Unit('N', 'newton', M=1, L=1, T=-2)
Pa = Unit('Pa', 'pascal', M=1, L=-1, T=-2)
J = Unit('J', 'joule', M=1, L=2, T=-2)
W = Unit('W', 'watt', M=1, L=2, T=-3)
C = Unit('C', 'coulomb', T=1, I=1)
V = Unit('V', 'volt', M=1, L=2, T=-3, I=-1)
Ohm = Unit('Ω', 'ohm', M=1, L=2, T=-3, I=-2)
S = Unit('S', 'siemens', M=-1, L=-2, T=3, I=2)
F = Unit('F', 'farad', M=-1, L=-2, T=4, I=2)
T = Unit('T', 'tesla', M=1, T=-2, I=-1)
Wb = Unit('Wb', 'weber', M=1, L=2, T=-2, I=-1)
H = Unit('H', 'henry', M=1, L=2, T=-2, I=-2)
degreesC = Unit('°C', 'celsius', THETA=1, offset=D('273.15'))
rad = Unit('rad', 'radian')
# sr = Unit('sr', 'steradian')
lm = Unit('lm', 'lumen', J=1)
lx = Unit('lx', 'lux', L=-2, J=1)
Bq = Unit('Bq', 'becquerel', T=-1)
Gy = Unit('Gy', 'gray', L=2, T=-2)
Sv = Unit('Sv', 'sievert', L=2, T=-2)
kat = Unit('kat', 'katal', T=-1, N=1)

# ----------------
# Imperial system
# ----------------
degreesF = Unit('°F', 'fahrenheit', THETA=1, offset=D('273.15') - D('32') / D('1.8'), coef=D('1') / D('1.8'))


UNITS = {
    # Basic SI units
    'm': m,
    'g': g,
    's': s,
    'A': A,
    'K': K,
    'mol': mol,
    'cd': cd,

    # Derived SI units
    'Hz': Hz,
    'N': N,
    'Pa': Pa,
    'J': J,
    'W': W,
    'C': C,
    'V': V,
    'Ω': Ohm,
    'S': S,
    'F': F,
    'T': T,
    'Wb': Wb,
    'H': H,
    '°C': degreesC,
    'rad': rad,
    # 'sr': sr,
    'lm': lm,
    'lx': lx,
    'Bq': Bq,
    'Gy': Gy,
    'Sv': Sv,
    'kat': kat,

    # Imperial system
    '°F': degreesF,
}
