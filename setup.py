#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Copyright (C) 2012 Karlisson Bezerra, contact@hacktoon.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

try:
    from setuptools import setup, find_packages
    extra = dict(tests_require=["nose"], test_suite="test", include_package_data=True)
except ImportError:
    from distutils.core import setup, find_packages
    extra = {}

import sys
setup(
    name = "ink2canvas",
    version = "0.0.1",
    description = "Inkscape extension exports SVG to HTML5 Canvas",
    author = "Karlisson Bezerra",
    author_email = "contact@hacktoon.com",
    url = "https://github.com/karlisson/ink2canvas",
    license = "GPLv2",
    packages = find_packages(),
    install_requires = [
        "lxml>=2.3",
    ],
    **extra
    )

