#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Sample from the data set.
"""

import sys
from math import log
from random import random
import argparse

# get number of records and partitions
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", type=int, default=10000)
parser.add_argument("-p", "--partition", type=int, default=3)
args = parser.parse_args()
n = args.number
p = args.partition

# calculate sampling probability
m = float(n) / p
rho = 1 / m * log(n * p)

# readable indexes
uid = 1
country, state, city = 2, 3, 4
topic, category, product = 5, 6, 7

# shortest regions of each batch
head = [(country,), (country, state, topic),
        (country, topic), (topic,)]

batch_number = len(head)


def read_input(file):
    """Read input and split."""
    for line in file:
        yield line.rstrip().split()


def main():
    data = read_input(sys.stdin)
    for e in data:
        if (random() < rho):  # sampling
            for batch in range(batch_number):
                # output: batch id|values of shortest region <TAB> uid
                print "%s|%s\t%s" % (str(batch),
                                     ' '.join(e[i] for i in head[batch]),
                                     e[uid])


if __name__ == "__main__":
    main()
