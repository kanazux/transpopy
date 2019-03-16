"""
Translate text from msgid's
"""

import re
import sys
from google.cloud import translate


def clean_text(_text):
    """clean_text: Clean msgid's text from a pot file

    :_text: list of msgid's text
    :returns: clean text, without 'msgid "' or '"'
    """

    _rawtext = ""
    for l in _text:
        _temptext = ""
        _temptext = re.sub(r'^msgid "', '', l)
        _temptext = re.sub(r'^"', '', _temptext)
        _temptext = re.sub(r'"\n', '\n', _temptext)
        _rawtext += _temptext

    return _rawtext


def clean_output_text(_text):
    """clean_output_text: Clean msgstr's text after translates

    :_text: list of msgid's text
    :returns: clean text, with 'msgstr "' and double quotes
    """

    _temp = ""
    _templist = _text.splitlines()
    _templistlen = len(_templist) - 1
    for i, l in enumerate(_templist):
        # Clean
        _temptext = l.rstrip()
        # https://github.com/Khan/polib/blob/master/polib.py
        # Escapes the characters ``\\\\``, ``\\t``, ``\\n``, ``\\r`` and ``"``
        # in the given string ``st`` and returns it.
        _temptext = _temptext.replace('\\', r'\\')\
                             .replace('\t', r'\t')\
                             .replace('\r', r'\r')\
                             .replace('\n', r'\n')\
                             .replace('\"', r'\"')

        # First line, add 'msg str "...' to the text
        if i == 0 and i == _templistlen:
            # Single line, do not insert space in the end
            _temp += 'msgstr "' + _temptext + '"\n'
        elif i == 0 and i != _templistlen and len(_temptext) > 0:
            # Multiple line, insert space in the end
            _temp += 'msgstr "' + _temptext + ' "\n'
        elif i == 0 and i != _templistlen and len(_temptext) == 0:
            # Multiple line and line empty, do not insert space in the end
            _temp += 'msgstr "' + _temptext + '"\n'
        elif i != 0 and i == _templistlen:
            # Last line, do not insert space in the end
            _temp += '"' + _temptext + '"\n'
        else:
            # It's not the firs or last line, insert space in the end
            _temp += '"' + _temptext + ' "\n'

    return _temp


def translate_text(_text, _targ_lang, _error=False, _print_process=False):
    """translate_text: Translate msgid text from a pot file

    :_text: msgid text
    :_targ_lang: translate text to this language
    :_error: save translated texts as fuzzy(draft)
    :_print_process: print translate errors if exist
    :returns: text translated
    """

    try:
        _client = translate.Client()
    except Exception as error:
        print(error)
        sys.exit(1)

    if _print_process:
        print('............................................................')
        print('Tranlating message:')
        print(clean_text(_text))
    try:
        # Preserve line breaks
        # The translate api has a parameter format which you can set to text.
        # This will preserve line breaks. See
        # https://cloud.google.com/translate/docs/reference/translate.
        trans = _client.translate(
                    clean_text(_text),
                    target_language=_targ_lang,
                    format_="text")
    except Exception as error:
        if _error:
            print(error)

    _newtext = clean_output_text(trans['translatedText'])

    if _print_process:
        print('-->')
        print(trans['translatedText'])

    return _newtext
