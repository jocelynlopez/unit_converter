#!/usr/bin/env python
# coding=utf-8

import re

from .exceptions import UnConsistentUnitsError, UnitDoesntExistError, PrefixDoesntExistError
from .units import Unit, PrefixUnit, UNITS, PREFIXES

VALUE_PATTERN = "[0-9]+.?[0-9]*"
UNIT_PATTERN = "[a-zA-Z]+"
VALUE_WITH_UNIT_REGEX = re.compile("(%s) *(%s)" % (VALUE_PATTERN, UNIT_PATTERN))
# (value_as_string, unit_as_string) = STRING_VALUE_REGEX.match('23.3 m').groups()


def get_basic_Unit_from_string(basic_unit_as_string):
    try:
        return UNITS[basic_unit_as_string]
    except KeyError:
        raise UnitDoesntExistError(basic_unit_as_string)


def get_prefix_from_string(prefix_as_string):
    try:
        factor = PREFIXES[prefix_as_string]['factor']
        name = PREFIXES[prefix_as_string]['name']
        return PrefixUnit(prefix_as_string, name, factor)
    except KeyError:
        raise PrefixDoesntExistError(prefix_as_string)


def extract_unit_from_basic_unit_and_prefix_as_string(unit_and_prefix_as_string):
    # Case with a prefix
    if unit_and_prefix_as_string[0] in PREFIXES.keys() and not unit_and_prefix_as_string[0] in ('m', 'T', 'd'):
        prefix_as_string = unit_and_prefix_as_string[0]
        unit_as_string = unit_and_prefix_as_string[1:]
    # Specific case :
    # ---------------
    #   da prefix (two letters prefix)
    elif unit_and_prefix_as_string[0] == 'd':
        if unit_and_prefix_as_string[0:2] == 'da':
            prefix_as_string = unit_and_prefix_as_string[0:2]
            unit_as_string = unit_and_prefix_as_string[2:]
        else:
            prefix_as_string = unit_and_prefix_as_string[0]
            unit_as_string = unit_and_prefix_as_string[1:]
    #   m prefix is also an unit : m = meter
    elif unit_and_prefix_as_string[0] == 'm' and len(unit_and_prefix_as_string) > 1:
        prefix_as_string = 'm'
        unit_as_string = unit_and_prefix_as_string[1:]
    #   T prefix is also an unit : T = Tesla
    elif unit_and_prefix_as_string[0] == 'T' and len(unit_and_prefix_as_string) > 1:
        prefix_as_string = 'T'
        unit_as_string = unit_and_prefix_as_string[1:]
    # Case with no prefix
    else:
        prefix_as_string = ''
        unit_as_string = unit_and_prefix_as_string

    return prefix_as_string, unit_as_string


def convert_from_string_to_Unit(prefix_as_string, unit_as_string):
    prefix = get_prefix_from_string(prefix_as_string)
    unit = get_basic_Unit_from_string(unit_as_string)
    return prefix * unit


class SmartUnitsConverter(object):

    def convert(self, value, desired_unit, current_unit=None):
        if not isinstance(desired_unit, Unit):
            if isinstance(desired_unit, str):
                prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(
                    desired_unit)
                desired_unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
        if current_unit and not isinstance(current_unit, Unit):
            if isinstance(current_unit, str):
                prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(
                    current_unit)
                current_unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
        if not isinstance(value, float) and not isinstance(value, int):
            if isinstance(value, str):
                value_as_string, unit_as_string = VALUE_WITH_UNIT_REGEX.match(value).groups()
                if unit_as_string:
                    prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(
                        unit_as_string)
                    current_unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
                value = float(value_as_string)

        return self.convert_value_with_unit_as_object(value, desired_unit, current_unit)

    @staticmethod
    def convert_value_with_unit_as_object(value, desired_unit, current_unit):
        if not current_unit.is_same_dimension(desired_unit):
            raise UnConsistentUnitsError(desired_unit.name, current_unit.name)
        ref_value = current_unit.offset + value * current_unit.coef
        desired_value = (-desired_unit.offset + ref_value) / desired_unit.coef
        return desired_value
