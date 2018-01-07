#!/usr/bin/env python
# -*- encoding=utf-8 -*-

from .converter import convert, converts
from .units import *

__title__ = 'unit_converter'
__version__ = '0.1.7'
__description__ = 'Package for converting quantities in different unit.'
__description__ += 'Currently, parsing quantities as string with or without units.'
__build__ = None
__author__ = 'Jocelyn LOPEZ'
__author_email__ = 'jocelyn.lopez.pro@gmail.com'
__url__ = 'https://bitbucket.org/jocelynlopez/unit_converter'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 Jocelyn LOPEZ'
__keywords__ = 'converter units sciences'

__all__ = [
    "convert", "converts",

    # Classes
    'SmartUnitsConverter',

    # Basic SI units
    'm',
    'g',
    's',
    'A',
    'K',
    'mol',
    'cd',

    # Derived SI units
    'Hz',
    'N',
    'Pa',
    'J',
    'W',
    'C',
    'V',
    'Ohm',
    'S',
    'F',
    'T',
    'Wb',
    'H',
    'degreesC',
    'rad',
    # 'sr': sr,
    'lm',
    'lx',
    'Bq',
    'Gy',
    'Sv',
    'kat',

    # Imperial system
    'degreesF', ]