#!/usr/bin/python3
"""Tests for ipy_data files"""


import re
from unittest import TestCase, main
from collections import defaultdict
from transpopy.po_data import po_data


class testPoData(TestCase):
    def test_po_data(self):
        self.assertIsInstance(po_data('samples/leap-seconds.po',
                                      False).get_msgs(), defaultdict)

class testiFuzzyData(TestCase):
    def test_fuzzy_data(self):
        self.assertIsInstance(po_data('samples/leap-seconds.po',
                                      True).get_msgs(), defaultdict)

class testGetHead(TestCase):
    def test_get_head(self):
        self.assertIsInstance(po_data(
            'samples/leap-seconds.po', True).get_head(), list)


if __name__ == "__main__":
    main()
