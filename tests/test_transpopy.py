#!/usr/bin/python3
"""Tests for ipy_data files"""


from argparse import ArgumentParser
from unittest import TestCase, main
from collections import defaultdict
from transpopy.po_data import po_data
from transpopy.transparse import return_args


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


class testReturnArgs(TestCase):
    def test_return_args(self):
        self.assertIsInstance(return_args(), ArgumentParser)


if __name__ == "__main__":
    main()
