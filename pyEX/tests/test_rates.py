# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import patch


class TestRates:
    def test_all(self):
        from pyEX import Client

        c = Client("test")
        with patch("pyEX.common._getIEXCloud"), patch("pickle.dump"):
            c.thirtyYear()
            c.twentyYear()
            c.tenYear()
            c.fiveYear()
            c.twoYear()
            c.oneYear()
            c.sixMonth()
            c.threeMonth()
            c.oneMonth()
