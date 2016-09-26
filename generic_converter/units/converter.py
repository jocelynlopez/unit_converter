#!/usr/bin/env python
# coding=utf-8

import re
from decimal import Decimal as D

from .exceptions import UnConsistentUnitsError, UnitDoesntExistError, PrefixDoesntExistError
from .units import Unit, PrefixUnit, UNITS, PREFIXES


# (value_as_string, unit_as_string) = STRING_VALUE_REGEX.match('23.3 m').groups()


# def build_unit_from_composed_units(composed_unit_as_string):
#     # First we needed to transform / operator into *^-1
#     composed_unit_as_string_without_div = composed_unit_as_string

#     for raw_basic_unit in composed_unit_as_string_without_div.split('*'):
#         basic_unit = raw_basic_unit.split('^')
#         if len(basic_unit) == 1:
#             prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(basic_unit[
#                                                                                                  0])
#             unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
#         elif len(basic_unit) == 2:
#             prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(basic_unit[
#                                                                                                  0])
#             unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
#             unit = unit**basic_unit[0]
#         else:
#             raise TypeError


class GlobalParser(object):

    VALUE_PATTERN = "[0-9]+.?[0-9]*"
    UNIT_PATTERN = "[°µΩa-zA-Z]+"
    VALUE_WITH_UNIT_REGEX = re.compile("(%s) *(%s)?" % (VALUE_PATTERN, UNIT_PATTERN))

    def __init__(self, *options):
        pass

    def get_value(self, string):
        value_as_string, units_as_string = self.VALUE_WITH_UNIT_REGEX.match(string).groups()
        return D(value_as_string)

    def get_units(self, string):
        value_as_string, units_as_string = self.VALUE_WITH_UNIT_REGEX.match(string).groups()
        if units_as_string:
            return BasicUnitParser().get_unit(units_as_string)
        else:
            return None


class BasicUnitParser(object):

    def __init__(self, *options):
        pass

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
            factor = PREFIXES[prefix_as_string]['factor']
            name = PREFIXES[prefix_as_string]['name']
            return PrefixUnit(prefix_as_string, name, factor)
        except KeyError:
            raise PrefixDoesntExistError(prefix_as_string)

    def get_unit(self, string):
        prefix = self.get_prefix(string)
        unit = self.get_default_unit(string)
        return prefix * unit


class BasicUnitConverter(object):
    """
    Converter for value with an unit.

    Limitations :
    -------------
        - only single units can be used (no composed unit like 'm/s')
        - only basic and derived SI units are available

    Examples :
    ----------

    >>> from generic_converter.units import BasicUnitConverter
    >>> converter = BasicUnitConverter()
    >>> converter.convert('2.78 dam', 'µm')
    Decimal('2.78E+7')
    """

    def convert(self, value, desired_unit, current_unit=None):

        if not isinstance(desired_unit, Unit):
            if isinstance(desired_unit, str):
                desired_unit = BasicUnitParser().get_unit(desired_unit)

        if current_unit and not isinstance(current_unit, Unit):
            if isinstance(current_unit, str):
                current_unit = BasicUnitParser().get_unit(current_unit)
        elif current_unit is None:
            current_unit = GlobalParser().get_units(value)

        if not isinstance(value, D):
            if isinstance(value, str):
                value = GlobalParser().get_value(value)
            else:
                raise TypeError("value argument need to be a 'decimal.Decimal' or string object !")

        return self.convert_value_with_unit_as_object(value, desired_unit, current_unit)

    @staticmethod
    def convert_value_with_unit_as_object(value, desired_unit, current_unit):
        if not current_unit.is_same_dimension(desired_unit):
            raise UnConsistentUnitsError(desired_unit.name, current_unit.name)
        ref_value = current_unit.offset + value * current_unit.coef
        desired_value = (-desired_unit.offset + ref_value) / desired_unit.coef
        return desired_value


class SmartUnitsConverter(BasicUnitConverter):
    pass

    # """
    # Converter for value with an unit.

    # Limitations :
    # -------------
    #     - only single units can be used (no composed unit like 'm/s')
    #     - only basic and derived SI units are available

    # Examples :
    # ----------

    # >>> from generic_converter.units import SmartUnitsConverter
    # >>> converter = SmartUnitsConverter()
    # >>> converter.convert('2.78 dam', 'µm')
    # Decimal('2.78E+7')
    # """

    # def convert(self, value, desired_unit, current_unit=None):
    #     if not isinstance(desired_unit, Unit):
    #         if isinstance(desired_unit, str):
    #             prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(
    #                 desired_unit)
    #             desired_unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
    #     if current_unit and not isinstance(current_unit, Unit):
    #         if isinstance(current_unit, str):
    #             prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(
    #                 current_unit)
    #             current_unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
    #     if not isinstance(value, D):
    #         if isinstance(value, str):
    #             value_as_string, unit_as_string = VALUE_WITH_UNIT_REGEX.match(value).groups()
    #             if unit_as_string:
    #                 prefix_as_string, unit_as_string = extract_unit_from_basic_unit_and_prefix_as_string(
    #                     unit_as_string)
    #                 current_unit = convert_from_string_to_Unit(prefix_as_string, unit_as_string)
    #             value = D(value_as_string)
    #         else:
    #             raise TypeError("value argument need to be a 'decimal.Decimal' or string object !")
    #     return self.convert_value_with_unit_as_object(value, desired_unit, current_unit)

    # @staticmethod
    # def convert_value_with_unit_as_object(value, desired_unit, current_unit):
    #     if not current_unit.is_same_dimension(desired_unit):
    #         raise UnConsistentUnitsError(desired_unit.name, current_unit.name)
    #     ref_value = current_unit.offset + value * current_unit.coef
    #     desired_value = (-desired_unit.offset + ref_value) / desired_unit.coef
    #     return desired_value

if __name__ == "__main__":
    import doctest
    doctest.testmod()
