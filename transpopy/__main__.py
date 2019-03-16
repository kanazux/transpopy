# -*- coding: utf-8 -*-
"""
Read and translate a POT file with Google API.

This script uses the Google Translate API to translate texts into a PO file.
It can set the translated texts as fuzzy (draft) optionally.
"""


import os
import re
import sys

from .transparse import return_args
from .translate import translate_text


def check_google_credentials(_help):
    """Check if Google credential exists in the shell environment."""

    _doc = ("https://cloud.google.com/"
            "docs/authentication/getting-started")
    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        print(("This script needs a Google Cloud Translate API credential.\n"
               "You need to export GOOGLE_APPLICATION_CREDENTIALS\n"
               "in the shell environment.\n"
               "Look at Google's documentation to know how to create\n"
               "an API key.\n"
               "\n  {}\n".format(_doc)))
        _help.print_help()
        sys.exit(1)


def mainmsg(_opts):
    """Main function of transpopy."""

    msgidcount = 0
    msgidmark = False
    msgctxtmark = False

    patternmsgid = re.compile('^msgid')
    patternmsgstr = re.compile('^msgstr')
    patternmsgtxt = re.compile('^"')
    patternmsgctxt = re.compile('^msgctxt "_"$')

    try:
        new_pofile = open(_opts.output_file, 'w')
    except Exception as error:
        print(error)
        sys.exit(1)

    try:
        testfile = open(_opts.file)
    except Exception as error:
        print(error)
        sys.exit(1)
    else:
        testfile.close()

    with open(_opts.file) as f:
        for line in f:

            if patternmsgctxt.match(line):
                # msgctxt "-" - FreeBSD pattern, skip next msgid
                msgctxtmark = True
                msgidcount += 1

                if _opts.imprecise and msgidcount > 1:
                    new_pofile.write('#, fuzzy\n')

            if patternmsgid.match(line):
                msgidmark = True
                msgidcount += 1
                msgtmp = []

                if _opts.imprecise and msgidcount > 1 and not msgctxtmark:
                    new_pofile.write('#, fuzzy\n')

                msgtmp.append(line)

            if patternmsgstr.match(line):
                # This is the msgid's end, it's time to translate() the text
                msgidmark = False
                msgctxtmark = False

                # Ignore the first msgid (Header)
                if msgidcount > 1:
                    # translate here
                    new_pofile.write(
                        translate_text(
                                msgtmp,
                                _opts.translate,
                                _opts.error,
                                _opts.print_process
                            )
                        )
                    continue

            if patternmsgtxt.match(line) and msgidmark:
                msgtmp.append(line)

            # Write to output file
            new_pofile.write("{}".format(line))

        new_pofile.close()


def main():
    parser = return_args()
    check_google_credentials(parser)

    opts = parser.parse_args()

    mainmsg(opts)
