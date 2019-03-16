#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Parse some options to transpopy."""


from argparse import ArgumentParser


def return_args():
    """Return a parser object."""
    _parser = ArgumentParser(add_help=True, description=(
        "Translate msgid's from a POT file with Google Translate API"))
    _parser.add_argument('-f', '--file', action='store', required=True,
                         help="Get the POT file name.")
    _parser.add_argument('-o', '--output_file', action='store', required=True,
                         help="Get name to save the new PO file.")
    _parser.add_argument('-t', '--translate', action='store', required=True,
                         help="Get language to translate to.")
    _parser.add_argument('-i', '--imprecise', action='store_true',
                         help="Save translated texts as fuzzy(draft).")
    _parser.add_argument('-e', '--error', action='store_true',
                         help="Print translate errors if exist.")
    _parser.add_argument('-p', '--print_process', action='store_true',
                         help="Print translate process.")
    return _parser
