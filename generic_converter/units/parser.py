#!/usr/bin/env python
# coding=utf-8

import re
from decimal import Decimal as D

from .exceptions import UnConsistentUnitsError, UnitDoesntExistError, PrefixDoesntExistError
from .units import Unit, PrefixUnit, UNITS, PREFIXES


class GlobalParser(object):

    VALUE_PATTERN = "[0-9]+.?[0-9]*"
    # UNIT_PATTERN = "[°µΩa-zA-Z/*^]+"
    UNIT_PATTERN = ".*"
    VALUE_WITH_UNIT_REGEX = re.compile("(%s) *(%s)?" % (VALUE_PATTERN, UNIT_PATTERN))

    def __init__(self, **options):
        self.options = options

    def get_value(self, string):
        value_as_string, units_as_string = self.VALUE_WITH_UNIT_REGEX.match(string).groups()
        return D(value_as_string)

    def get_units(self, string):
        value_as_string, units_as_string = self.VALUE_WITH_UNIT_REGEX.match(string).groups()
        return units_as_string
        # if units_as_string:
        #     return BasicUnitParser().get_unit(units_as_string)
        # else:
        #     return None


class BasicUnitParser(object):

    def __init__(self, **options):
        self.options = options

    @staticmethod
    def get_default_unit(string):

        first_letter = string[0]
        # Case with a prefix
        if first_letter in PREFIXES.keys() and not first_letter in ('m', 'T', 'd'):
            unit_as_string = string[1:]

        #   da prefix (two letters prefix)
        elif first_letter == 'd':
            if string[0:2] == 'da':
                unit_as_string = string[2:]
            else:
                unit_as_string = string[1:]

        #   m prefix is also an unit : m = meter
        elif first_letter == 'm' and len(string) > 1:
            unit_as_string = string[1:]

        #   T prefix is also an unit : T = Tesla
        elif first_letter == 'T' and len(string) > 1:
            unit_as_string = string[1:]

        # Case with no prefix
        else:
            unit_as_string = string

        try:
            return UNITS[unit_as_string]
        except KeyError:
            raise UnitDoesntExistError(unit_as_string)

    @staticmethod
    def get_prefix(string):

        first_letter = string[0]
        # Case with a prefix
        if first_letter in PREFIXES.keys() and not first_letter in ('m', 'T', 'd'):
            prefix_as_string = first_letter

        #   da prefix (two letters prefix)
        elif first_letter == 'd':
            if string[0:2] == 'da':
                prefix_as_string = string[0:2]
            else:
                prefix_as_string = first_letter

        #   m prefix is also an unit : m = meter
        elif first_letter == 'm' and len(string) > 1:
            prefix_as_string = first_letter

        #   T prefix is also an unit : T = Tesla
        elif first_letter == 'T' and len(string) > 1:
            prefix_as_string = first_letter

        # Case with no prefix
        else:
            prefix_as_string = ''

        try:
            return PREFIXES[prefix_as_string]
        except KeyError:
            raise PrefixDoesntExistError(prefix_as_string)

    def get_unit(self, string):
        prefix = self.get_prefix(string)
        unit = self.get_default_unit(string)
        return prefix * unit


class ComposedUnitParser(object):

    def __init__(self, **options):
        self.options = options

    def build_unit_from_composed_units(composed_unit_as_string):
        # First we needed to transform / operator into *^-1
        composed_unit_as_string_without_div = composed_unit_as_string

        for raw_basic_unit in composed_unit_as_string_without_div.split('*'):
            basic_unit = raw_basic_unit.split('^')
            if len(basic_unit) == 1:
                unit = BasicUnitParser().get_unit(basic_unit[0])
            elif len(basic_unit) == 2:
                unit = BasicUnitParser().get_unit(basic_unit[0])
                unit = unit**basic_unit[0]
            else:
                raise TypeError
