Generic Converter
-----------------

![https://img.shields.io/docker/automated/negetem/python.svg](https://img.shields.io/docker/automated/negetem/python.svg)

Description
+++++++++++

Packages for converting units values.

Basic usages
++++++++++++

```
>>> from generic_converter.units import SmartUnitsConverter
>>>
>>> converter = SmartUnitsConverter()
>>> converter.convert('2.78 dam', 'µm')
>>> Decimal('2.78E+7')

```

Note: It is necessary to provide the value as a string. Indeed, the high precision of conversion (1E-27) is possible only with string, by using Decimal object in replacement of float object.

Contributing
++++++++++++
Please submit and comment on bug reports and feature requests.

To submit a patch:

1. Fork it (https://bitbucket.org/negetem/generic_converter/fork).
2. Create your feature branch (`git checkout -b my-new-feature`).
3. Make changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin my-new-feature`).
6. Create a new Pull Request.

License
+++++++
This app is licensed under the MIT license.

Warranty
++++++++
This software is provided "as is" and without any express or
implied warranties, including, without limitation, the implied
warranties of merchantibility and fitness for a particular
purpose.
