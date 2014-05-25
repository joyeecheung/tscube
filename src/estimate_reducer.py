#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Split the sample into p intervals,
    output the p-1 boundaries.
"""

import sys

# arguments that need to be manually configured
p = 3  # number of partitions
# configuration ends


def read_input(file):
    """Read input and split."""
    for line in file:
        yield line.rstrip()


def main():
    data = sorted(read_input(sys.stdin))
    size = len(data)
    for i in range(size / p, size - size / p + 1, size / p):
        print data[i]


if __name__ == "__main__":
    main()
