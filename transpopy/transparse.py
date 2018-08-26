#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Parse some options to transpopy."""


from argparse import ArgumentParser


def return_args():
    """Return a parser object."""
    _parser = ArgumentParser(add_help=True, description=(
        "Translate msgid from po file with google translate API"))
    _parser.add_argument('-f', '--file', action='store', required=True,
                         help="Get the po file name to translated msgid's.")
    _parser.add_argument('-o', '--output_file', action='store', required=True,
                         help="Get a name to save new po file.")
    _parser.add_argument('-l', '--lang', action='store', required=False,
                         help="Get original language of po file.")
    _parser.add_argument('-t', '--translate', action='store', required=True,
                         help="Get language to translate the po file strings.")
    _parser.add_argument('-i', '--imprecise', action='store_true',
                         help="Write messages as fuzzy.")
    _parser.add_argument('-e', '--error', action='store_true',
                         help="Print some errors if exists.")
    _parser.add_argument('-p', '--print_process', action='store_true',
                         help="Print translate process.")
    return _parser
