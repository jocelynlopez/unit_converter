#!/usr/bin/env python
# coding=utf-8

import re
from functools import reduce

from .units import PREFIXES, UNITS, Unit
from .exceptions import UnitDoesntExistError


class UnitParser(object):
    unit_re = re.compile("(?P<unit>[a-zA-Z°Ωµ])+\^?(?P<pow>[-+]?[0-9]*\.?[0-9]*)")
    unit_re_without_group = re.compile("[a-zA-Z°Ωµ]+\^?[-+]?[0-9]*\.?[0-9]*")

    def parse(self, unit: str) -> Unit:
        l_unit_s = self.unit_re_without_group.findall(unit)
        l_unit = list(map(self._parse_unit, l_unit_s))
        return reduce(lambda x, y: x * y, l_unit)

    def _parse_unit(self, unit: str) -> Unit:
        r = self.unit_re.match(unit)
        power = float(r.group("pow"))
        unit = self._parse_simple_unit(r.group("unit"))
        return unit**power

    @staticmethod
    def _parse_simple_unit(unit: str) -> Unit:
        """Parse a simple unit.

        In other word, parse an unit without a power value.
        """
        # TODO: Refactoring for an automatic distinction between unit and prefix
        # Case with a prefix
        if unit[0] in PREFIXES.keys() and unit[0] not in 'mTd':
            prefix = unit[0]
            unit_without_prefix = unit[1:]

        #   da prefix (two letters prefix)
        elif unit[0] == 'd':
            if unit[0:2] == 'da':
                prefix = 'da'
                unit_without_prefix = unit[2:]
            else:
                prefix = unit[0]
                unit_without_prefix = unit[1:]

        #   m prefix is also an unit : m = meter
        elif unit[0] == 'm' and len(unit) > 1:
            prefix = unit[0]
            unit_without_prefix = unit[1:]

        #   T prefix is also an unit : T = Tesla
        elif unit[0] == 'T' and len(unit) > 1:
            prefix = unit[0]
            unit_without_prefix = unit[1:]

        # Case with no prefix
        else:
            prefix = ''
            unit_without_prefix = unit

        try:
            return PREFIXES[prefix]*UNITS[unit_without_prefix]
        except KeyError:
            raise UnitDoesntExistError(unit_without_prefix)


class QuantityParser(object):
    def __init__(self, decimal_mark='.'):
        self.decimal_mark = decimal_mark