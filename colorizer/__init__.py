#!/usr/bin/env python
"""
Console output colorizator
Author: Alexander Artemenko <svetlyak.40wt@gmail.com>
Usage: tail -f some.log | colorize 'one.*pattern' 'another'
"""

import sys
import re

from termcolor import colored, COLORS
from itertools import starmap


COLORS = sorted([c for c in COLORS.keys() if c != 'grey'])

class Colorer:
    def __init__(self, regex, color):
        self.regex = re.compile(regex)
        self.color = color

    def __call__(self, line):
        return self.regex.sub(lambda x: colored(x.group(0), self.color), line)

COLORERS = list(starmap(Colorer, zip(sys.argv[1:], COLORS)))

def process(line):
    for colorer in COLORERS:
        line = colorer(line)
    return line


def main():
    if len(sys.argv) == 1:
        sys.stderr.write("Usage: tail -f some.log | %s 'one.*pattern' 'another'\n" % sys.argv[0])
        sys.exit(1)

    if len(sys.argv[1:]) > len(COLORS):
        sys.stderr.write('Num arguments should not be more than %s.\n' % len(COLORS))
        sys.exit(1)

    for line in sys.stdin.xreadlines():
        sys.stdout.write(process(line))

if __name__ == '__main__':
    main()

