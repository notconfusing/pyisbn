#
#
"""test_sbn - Test Sbn class"""
# Copyright (C) 2007-2012  James Rowe
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from unittest import TestCase

from expecter import expect
from nose2.tools import params

from pyisbn import Sbn


class TestSbn(TestCase):
    def test___repr__(self):
        expect(repr(Sbn('521871723'))) == "Sbn('521871723')"

    @params(
        ('07114816', '7'),
        ('071148167', '7'),
    )
    def test_calculate_checksum(self, sbn, result):
        expect(Sbn(sbn).calculate_checksum()) == result

    def test_convert(self):
        expect(Sbn('071148167').convert()) == '9780071148160'