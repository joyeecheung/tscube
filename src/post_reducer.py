#!/usr/bin/env python
import sys
from itertools import product
from operator import itemgetter
from itertools import groupby


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    # f = open('mapped')
    # data = [line for line in read_input(f)]
    data = read_input(sys.stdin)
    for cur_group, groups in groupby(data, itemgetter(0)):
        # values = [int(measure) for attr, measure in groups]
        # print "cur_group", cur_group
        # print "values", values
        print "%s\t%s" % (cur_group,
                          sum(int(measure) for attr, measure in groups))

if __name__ == "__main__":
    main()
