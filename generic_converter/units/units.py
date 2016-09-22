#!/usr/bin/env python
# coding=utf-8

PREFIXES = {
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


class PrefixUnit(object):

    def __init__(self, symbol, name=None, factor=None):
        self.symbol = symbol

        if not name:
            self.name = PREFIXES[self.symbol]['name']
        else:
            self.name = name

        if not name:
            self.factor = PREFIXES[self.symbol]['factor']
        else:
            self.factor = factor

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
        return (self.L == other_unit.L and
                self.M == other_unit.M and
                self.T == other_unit.T and
                self.I == other_unit.I and
                self.THETA == other_unit.THETA and
                self.N == other_unit.N and
                self.J == other_unit.J)


#---------------
# Basic SI units
# --------------
m = Unit('m', 'meter', L=1)
g = Unit('g', 'gram', M=1, coef=1E-3)
s = Unit('s', 'second', T=1)
A = Unit('A', 'ampere', I=1)
K = Unit('K', 'kelvin', THETA=1)
mol = Unit('mol', 'mole', N=1)
cd = Unit('cd', 'candela', J=1)


# ----------------
# Derived SI units
# ----------------
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
T = Unit('T', M=1, T=-2, I=-1)
Wb = Unit('Wb', 'weber', M=1, L=2, T=-2, I=-1)
H = Unit('H', 'henry', M=1, L=2, T=-2, I=-2)
degreesC = Unit('°C', 'celsius', THETA=1, offset=273.15)
rad = Unit('rad', 'radian')
# sr = Unit('sr', 'steradian')
lm = Unit('lm', 'lumen', J=1)
lx = Unit('lx', 'lux', L=-2, J=1)
Bq = Unit('Bq', 'becquerel', T=-1)
Gy = Unit('Gy', 'gray', L=2, T=-2)
Sv = Unit('Sv', 'sievert', L=2, T=-2)
kat = Unit('kat', 'katal', T=-1, N=1)

# ---------------
# Imperial system
# ---------------
degreesF = Unit('°F', 'fahrenheit', THETA=1, offset=273.15 - 32 / 1.8, coef=1 / 1.8)


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
