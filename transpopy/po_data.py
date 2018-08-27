#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a defultdict from pofile

Translate strings from google nltk and put po data with translted strings
on a new po file.
"""


import re
from collections import defaultdict


class po_data():

    def __init__(self, _file, _fuzzy=False):
        """Init some variables."""

        with open(_file, 'r') as _open_file:
            self.data = list(filter(None, _open_file.read().split("\n")))
        self.head = []
        self.msgs = defaultdict(lambda: False)
        self.fuzzy = _fuzzy
        if self.fuzzy:
            self.msgid = "#~ msgid"
            self.msgstr = "#~ msgstr"
        else:
            self.msgid = "msgid"
            self.msgstr = "msgstr"

    def get_head(self):
        """Get head of file, dont translate this part of document."""

        for line in self.data:
            if bool(re.match(r"^#[:|~|\.]", line)):
                break
            else:
                self.head.append(line.strip())
        return self.head

    def get_msgs(self):
        """Read the po file and get messages to translate.

        Save lines references as like msgstr.
        Return a defaultdict with msgid like iterator items and msgstr into
        a dict key ['msgstr'].
        """

        _data = self.data[len(self.get_head()):]
        for idx, line in enumerate(_data):
            if line.startswith(self.msgid):
                _msgid = []
                _msgid.append(re.split(r"^{}".format(self.msgid),
                                       line)[-1].strip())
                _cont = 1
                while True:
                    if _data[idx + _cont].startswith(self.msgstr):
                        break
                    else:
                        _msgid.append(_data[idx + _cont])
                        _cont += 1
                _msgid = "|\n|".join([l for l in _msgid])
                self.msgs[_msgid] = defaultdict(lambda: False)
                self.msgs[_msgid]['lines'] = []
                if not self.fuzzy:
                    _cont = 1
                    while True:
                        _lines = _data[idx - _cont]
                        if not _lines.startswith('#'):
                            break
                        else:
                            self.msgs[_msgid]['lines'].append(_lines)
                        _cont += 1
                self.msgs[_msgid]['msgstr'] = []
            if line.startswith(self.msgstr):
                self.msgs[_msgid]['msgstr'].append(
                    re.split(r"^{}".format(self.msgstr), line)[-1].strip())
                _cont = 1
                while True:
                    try:
                        _msgstr = _data[idx + _cont]
                        if _msgstr.startswith("#") or _msgstr.startswith(
                                self.msgid):
                            break
                        else:
                            self.msgs[_msgid]['msgstr'].append(_msgstr)
                        _cont += 1
                    except IndexError:  # pragma: no cover
                        break
        return self.msgs
