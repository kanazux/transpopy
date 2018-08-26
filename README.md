# transpopy
Read pot files to translate strings in msgid with google translate API and save a new po file.

### Usage:
> transpopy -f samples/leap-seconds.pot -o newfile.po -t pt_br -e -i -p

### Help:
Translate msgid from po file with google translate API

```
optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Get the po file name to translated msgid's.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Get a name to save new po file.
  -l LANG, --lang LANG  Get original language of po file.
  -t TRANSLATE, --translate TRANSLATE
                        Get language to translate the po file strings.
  -i, --imprecise       Write messages as fuzzy.
  -e, --error           Print some errors if exists.
  -p, --print_process   Print translate process.
```
