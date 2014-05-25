#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Split the sample into p intervals,
    output the p-1 boundaries.
"""

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--partition", type=int, default=3)

args = parser.parse_args()
p = args.partition


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
