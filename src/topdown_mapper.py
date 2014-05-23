#!/usr/bin/env python
import sys
from bisect import bisect_left

uid = 1
country, state, city = 2, 3, 4
topic, category, product = 5, 6, 7

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
    for line in file:
        yield line.rstrip().split()


def main():
    pt_f = open('partition_lst', 'r')
    boundaries = [line.rstrip() for line in pt_f]
    data = read_input(sys.stdin)
    for e in data:
        for batch in range(batch_number):
            head = "%s|%s" % (str(batch), ' '.join(e[i] for i in C[batch][-1]))
            part = "%s|%s\t%s" % (str(batch),
                                  ' '.join(e[i] for i in C[batch][-1]),
                                  e[uid])
            pid = bisect_left(boundaries, part)
            fields = ' '.join(e[i] for i in C[batch][0])
            print "%d\t%s\t%s\t%s" % (pid, e[uid], head, fields)

if __name__ == "__main__":
    main()
