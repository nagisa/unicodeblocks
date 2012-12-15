#!/usr/bin/env python3
""" A tool to generate a python parseable list of block names and staring/
ending sequences from http://www.unicode.org/Public/UNIDATA/Blocks.txt """

from urllib import request
import os
import os.path

uri = 'http://www.unicode.org/Public/UNIDATA/Blocks.txt'
root = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(root, 'unicodeblocks', 'blocklist.py')

with open(target_path, 'w') as f, request.urlopen(uri) as req:
    f.write('blocks = [\n')
    for lineno, line in enumerate(req):
        line = line.decode('utf-8')
        # Skip comment or empty lines
        if line.startswith('#') or line.strip() == '':
            if lineno == 0:
                print(line, end='')
            continue
        codepoints, name = line.strip().split(';')
        start, end = codepoints.split('..')
        start, end, name = start.strip(), end.strip(), name.strip()
        f.write('    ("{2}", 0x{0}, 0x{1}),\n'.format(start, end, name))
    f.write(']\n')
