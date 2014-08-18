#!/usr/bin/python 
import sys
import types

from collections import OrderedDict

class MutableNamedTuple(OrderedDict):
    def __init__(self, *args, **kwargs):
        super(MutableNamedTuple, self).__init__(*args, **kwargs)
        self._initialized = True

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if hasattr(self, '_initialized'):
            super(MutableNamedTuple, self).__setitem__(name, value)
        else:
            super(MutableNamedTuple, self).__setattr__(name, value)
