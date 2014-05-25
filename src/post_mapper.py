#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Pipe the k-v pair trough.
"""

import sys
from itertools import product


def read_input(file):
    """Read input."""
    for line in file:
        yield line.rstrip()


def main():
    data = read_input(sys.stdin)
    for e in data:
        print e


if __name__ == "__main__":
    main()
