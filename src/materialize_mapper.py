#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Output the tuple for each batch, with corresponding
    partition ID.
"""

import sys
from bisect import bisect_left

# readable indexes
uid = 1
country, state, city = 2, 3, 4
topic, category, product = 5, 6, 7

# batching plan
C = [(
    (country, state, city, topic, category, product),
    (country, state, city, topic, category),
    (country, state, city, topic),
    (country, state, city),
    (country, state),
    (country,)
), (
    (country, state, topic, category, product),
    (country, state, topic, category),
    (country, state, topic)
), (
    (country, topic, category, product),
    (country, topic, category),
    (country, topic)
), (
    (topic, category, product),
    (topic, category),
    (topic,)
)]

batch_number = len(C)


def read_input(file):
    """Read input and split."""
    for line in file:
        yield line.rstrip().split()


def main():
    # get boundaries from the partition file
    pt_f = open('partition_lst', 'r')
    boundaries = [line.rstrip() for line in pt_f]
    pt_f.close()

    data = read_input(sys.stdin)
    for e in data:
        for batch in range(batch_number):
            # get: batch id|value of the shortest region
            head = "%s|%s" % (str(batch), ' '.join(e[i] for i in C[batch][-1]))

            # find the partition in this batch for the tuple
            part = "%s\t%s" % (head, e[uid])
            pid = bisect_left(boundaries, part)

            fields = ' '.join(e[i] for i in C[batch][0])
            print "%d\t%s\t%s\t%s" % (pid, e[uid], head, fields)

if __name__ == "__main__":
    main()
