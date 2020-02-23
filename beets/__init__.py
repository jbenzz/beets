# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2016, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

from __future__ import division, absolute_import, print_function

import os

import confuse

__version__ = u'1.5.0'
__author__ = u'Adrian Sampson <adrian@radbox.org>'


class IncludeLazyConfig(confuse.LazyConfig):
    """A version of Confuse's LazyConfig that also merges in data from
    YAML files specified in an `include` setting.
    """
    def read(self, user=True, defaults=True):
        super(IncludeLazyConfig, self).read(user, defaults)

        try:
            for view in self['include']:
                filename = view.as_filename()
                if os.path.isfile(filename):
                    self.set_file(filename)
                else:
                    raise FileNotFoundError("Warning! Configuration file({0}) "
                                            "does not exist!".format(filename))
        except confuse.NotFoundError:
            pass


config = IncludeLazyConfig('beets', __name__)
