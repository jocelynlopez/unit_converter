
**************
Unit Converter
**************

Description
===========

Package for converting quantities into different units.


Basic usages
============

>>> from unit_converter.converter import convert, converts
>>>
>>> convert('2.78 daN*mm^2', 'mN*µm^2')
>>> Decimal('2.78E+10')
>>>
>>> converts('2.78 daN*mm^2', 'mN*µm^2')
>>> '2.78E+10'
>>>
>>> converts('78 min', 'h')
>>> '1.3'
>>>
>>> converts('52°C', '°F')
>>> '125.6'
>>>
>>> converts('120 km*h^-1', 'mile*h^-1')
>>> '74.56454306848007635409210214'



Note: It is necessary to provide the value as a string. Indeed, the high precision of conversion (1E-27) is possible only with string, by using Decimal object in replacement of float object.

Contributing
============
Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://bitbucket.org/negetem/unit_converter/fork).
2. Create your feature branch (*git checkout -b my-new-feature*).
3. Make changes.
4. Commit your changes (*git commit -am 'Add some feature'*).
5. Push to the branch (*git push origin my-new-feature*).
6. Create a new Pull Request.

License
=======
This app is licensed under the MIT license.

Warranty
========
This software is provided "as is" and without any express or
implied warranties, including, without limitation, the implied
warranties of merchantibility and fitness for a particular
purpose.


***************
Release History
***************

0.0.1 (2016-09-21)
==================
- Initial release

0.1.1 (2016-09-27)
==================

**Improvements**

- Added support for combined units like '**kg*m*s^-2**'

1.0.0 (2018-01-16)
==================

**Improvements**

- Big code refactoring
- Added handy functions convert and converts (return a string)

1.1.0 (2018-01-16)
==================

**Improvements**

- Add handling french format number 78,6 instead of 78.6

**Tests**
- Check if all prefix + unit are unique