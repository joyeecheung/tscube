#!/usr/bin/env python

import sys
from math import log
from random import random

n = 10000
p = 1
m = float(n) / p
rho = 1 / m * log(n * p)

uid = 1
country, state, city = 2, 3, 4
topic, category, product = 5, 6, 7

head = [(country,), (country, state, topic),
        (country, topic), (topic,)]

batch_number = len(head)


def read_input(file):
    for line in file:
        yield line.rstrip().split()


def main():
    data = read_input(sys.stdin)
    for e in data:
        if (random() < rho):
            for batch in range(batch_number):
                # batch_head | head_value <TAB> country, ..., product uid
                print "%s|%s\t%s" % (str(batch),
                                     ' '.join(e[i] for i in head[batch]),
                                     e[uid])
if __name__ == "__main__":
    main()
