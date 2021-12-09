#!/usr/bin/env python
"""Mapper outputs Make and year with count of it."""
import sys


# input comes from STDIN (standard input)
def mapper(input):
    for line in input:
        row = str(line).strip()
        # Data        # Return
        print '%s\t%s' % (row, 1)


def main(input):
    mapper(input)


if __name__ == "__main__":
    input = sys.stdin
    main(input)
