#!/usr/bin/env python
# coding=utf-8

import re
from functools import reduce

from .units import PREFIXES, UNITS, Unit
from .exceptions import UnitDoesntExistError


class UnitParser(object):
    unit_re = re.compile("(?P<unit>[a-zA-Z°Ωµ])+\^?(?P<pow>[-+]?[0-9]*\.?[0-9]*)")

    def parse(self, unit: str) -> Unit:
        l_unit_s = self.unit_re.findall(unit)
        l_unit = list(map(self._parse_unit, l_unit_s))
        return reduce(lambda x, y: x * y, l_unit)

    def _parse_unit(self, unit: str, power: str) -> Unit:
        return self._parse_simple_unit(unit)**float(power)

    @staticmethod
    def _parse_simple_unit(unit_s: str) -> Unit:
        """Parse a simple unit.

        In other word, parse an unit without a power value.
        """
        unit = None
        for prefix in PREFIXES.keys():
            if unit_s.startswith(prefix) and unit_s[len(prefix):] in UNITS.keys():
                prefix = PREFIXES[prefix]
                unit = UNITS[unit_s[len(prefix):]]
                exit
        
        if unit is None:
            raise UnitDoesntExistError(unit_s)

        return prefix*unit


class QuantityParser(object):

    quantity_re = re.compile("(?P<value>\d+[.,]?\d*) *(?P<unit>.*)")

    def parse(self, quantity: str) -> tuple:
        r = self.quantity_re.match(quantity)
        value = float(r.group("value"))
        unit = UnitParser().parse(r.group("unit")) 
        return value*unit
