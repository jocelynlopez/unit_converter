#!/usr/bin/env python
# coding=utf-8


class UnConsistentUnitsError(ValueError):

    def __init__(self, *args):
        if args:
            self.value = "Units %s are not of the same dimension !" % str(args)
        else:
            self.value = "Units are not of the same dimension !"

    def __str__(self):
        return repr(self.value)


class UnitDoesntExistError(ValueError):

    def __init__(self, *args):
        if args:
            self.value = "Unit %s doesn't exist !" % str(args)
        else:
            self.value = "Unit doesn't exist !"

    def __str__(self):
        return repr(self.value)


class PrefixDoesntExistError(ValueError):

    def __init__(self, *args):
        if args:
            self.value = "Prefix %s doesn't exist !" % str(args)
        else:
            self.value = "Prefix doesn't exist !"

    def __str__(self):
        return repr(self.value)
