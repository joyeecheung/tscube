#!/usr/bin/env python

import sys
from itertools import groupby
from operator import itemgetter

country, state, city = '2', '3', '4'
topic, category, product = '5', '6', '7'

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


def read_input(file):
    for line in file:
        # (uid, head, fields)
        yield line.rstrip().split('\t')[1:]


def main():
    data = read_input(sys.stdin)

    # for each batch
    for head, group in groupby(data, itemgetter(1)):
        batch = int(head.split('|')[0])
        b_size = len(C[batch][0])
        b_min_size = len(C[batch][-1])
        cur_value = []
        cur_set = []
        for triple in group:
            fields = triple[-1].split(' ')
            uid = triple[0]
            if not cur_value:
                cur_value = fields[:]
                cur_set = [set((uid, )) for i in range(b_size)]

            # for i in range(b_size - 1, b_min_size - 2, -1):
            for i in range(b_min_size - 1, b_size, 1):
                if fields[i] != cur_value[i]:
                    for j in range(i, b_size, 1):
                        val = ' '.join(cur_value[:j + 1])
                        attr = ' '.join(j for j in C[batch][0][:j + 1])
                        print "%s|%s\t%s" % (attr, val, len(cur_set[j]))
                        cur_set[j].clear()
                        cur_set[j].add(uid)

                    cur_value[i:] = fields[i:]
                    break

                else:
                    cur_set[i].add(uid)

        for i in range(b_size - 1, b_min_size - 2, -1):
            val = ' '.join(cur_value[:i + 1])
            attr = ' '.join(j for j in C[batch][0][:i + 1])
            print "%s|%s\t%s" % (attr, val, len(cur_set[i]))


if __name__ == "__main__":
    main()
