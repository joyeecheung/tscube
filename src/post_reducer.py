#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Merge all groups.
"""

import sys
from itertools import product
from operator import itemgetter
from itertools import groupby


def read_input(file):
    """Read inpu and split."""
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = read_input(sys.stdin)
    for cur_group, groups in groupby(data, itemgetter(0)):
        print "%s\t%s" % (cur_group,
                          sum(int(measure) for attr, measure in groups))


if __name__ == "__main__":
    main()
