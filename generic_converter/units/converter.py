#!/usr/bin/env python
# coding=utf-8

import re
from decimal import Decimal as D

from .exceptions import UnConsistentUnitsError
from .units import Unit, UnitPrefix, UNITS, PREFIXES
from .parser import GlobalParser, BasicUnitParser


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

        # Convert desired_unit in an Unit object if needed
        if isinstance(desired_unit, str):
            desired_unit = BasicUnitParser().get_unit(desired_unit)
        elif not isinstance(desired_unit, Unit):
            raise TypeError("desired_unit argument need to be a 'units.Unit' or string object !")

        # Convert current_unit in an Unit object if needed
        if current_unit is None:
            unit_as_string = GlobalParser().get_units(value)
            current_unit = BasicUnitParser().get_unit(unit_as_string)
        elif isinstance(current_unit, str):
            current_unit = BasicUnitParser().get_unit(current_unit)
        elif not isinstance(current_unit, Unit):
            raise TypeError("current_unit argument need to be a 'units.Unit' or string object or None !")

        # Convert value in a Decimal object
        if isinstance(value, str):
            value = GlobalParser().get_value(value)
        elif not isinstance(value, D):
            raise TypeError("value argument need to be a 'decimal.Decimal' or string object !")

        # Check dimension from current and desired units
        if not current_unit.is_same_dimension(desired_unit):
            raise UnConsistentUnitsError(desired_unit.name, current_unit.name)

        return self.convert_to_desired_unit(value, desired_unit, current_unit)

    @staticmethod
    def convert_to_default_unit(value, current_unit):
        """Get converted value in the default unit."""
        return current_unit.offset + value * current_unit.coef

    def convert_to_desired_unit(self, value, desired_unit, current_unit):
        # Get converted value in the desired unit
        default_value = self.convert_to_default_unit(value, current_unit)
        desired_value = (-desired_unit.offset + default_value) / desired_unit.coef
        return desired_value


class SmartUnitsConverter(BasicUnitConverter):
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
