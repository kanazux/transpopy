#!/usr/bin/python3
"""Tests for transpopy files"""


from argparse import ArgumentParser
from unittest import TestCase, main
from transpopy.translate import clean_text, clean_output_text
from transpopy.transparse import return_args


class testReturnArgs(TestCase):
    def test_return_args(self):
        self.assertIsInstance(return_args(), ArgumentParser)


class testTranslateText(TestCase):
    def test_one_clean(self):
        textOriginal = '"Introduction"'
        textExpected = 'Introduction'
        result = clean_text(textOriginal)
        self.assertEqual(result, textExpected)

    def test_two_clean(self):
        textOriginal = '""'
        textExpected = ''
        result = clean_text(textOriginal)
        self.assertEqual(result, textExpected)

    def test_three_clean(self):
        textOriginal = '"Leap seconds are inserted at the same instant all over the world: "'
        textExpected = 'Leap seconds are inserted at the same instant all over the world: '
        result = clean_text(textOriginal)
        self.assertEqual(result, textExpected)

    def test_one_output(self):
        """ Single line """
        textOriginal = 'FreeBSD Support for Leap Seconds'
        textExpected = 'msgstr "FreeBSD Support for Leap Seconds"\n'
        result = clean_output_text(textOriginal)
        self.assertEqual(result, textExpected)
        clean_output_text

    def test_two_output(self):
        """ Multiple line, single """

        self.maxDiff = None

        textOriginal = '\n' \
            'A <emphasis>leap second</emphasis> is an one second adjustment made at\n' \
            'specific times of year to UTC to synchronize atomic time scales with\n' \
            'variations in the rotation of the Earth. This article describes how FreeBSD\n' \
            'interacts with leap seconds.'
        textExpected = 'msgstr ""\n' \
            '"A <emphasis>leap second</emphasis> is an one second adjustment made at "\n' \
            '"specific times of year to UTC to synchronize atomic time scales with "\n' \
            '"variations in the rotation of the Earth. This article describes how FreeBSD "\n' \
            '"interacts with leap seconds."\n'

        result = clean_output_text(textOriginal)
        self.assertEqual(result, textExpected)
        clean_output_text

    def test_three_output(self):
        """ Multiple line, with double quotes inside """

        self.maxDiff = None

        textOriginal = '\n' \
            'This does a similar thing to <_:buildtarget-1/>, but it does it only for\n' \
            'files with the given suffix. The suffix must have been defined already. Look\n' \
            'at Search Paths (<xref linkend=\"searchpaths\"/>) for more information.'
        textExpected = 'msgstr ""\n' \
            '"This does a similar thing to <_:buildtarget-1/>, but it does it only for "\n' \
            '"files with the given suffix. The suffix must have been defined already. Look "\n' \
            '"at Search Paths (<xref linkend=\\\"searchpaths\\\"/>) for more information."\n'

        result = clean_output_text(textOriginal)
        self.assertEqual(result, textExpected)
        clean_output_text


if __name__ == "__main__":
    main()
