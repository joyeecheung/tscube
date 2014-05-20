#!/usr/bin/env python
import sys
from bisect import bisect_left

uid = 1
country, state, city = 2, 3, 4
topic, category, product = 5, 6, 7

p = 4

# C = [(
#     (country,),
#     (country, state),
#     (country, state, city),
#     (country, state, city, topic),
#     (country, state, city, topic, category),
#     (country, state, city, topic, category, product)
# ), (
#     (topic,),
#     (topic, country),
#     (topic, country, state),
#     (topic, category, country, state),
#     (topic, category, product, country, state)
# ), (
#     (topic, category),
#     (topic, category, country),
#     (topic, category, product, country)
# ), (
#     (topic, category, product),
# )]

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

useful = (country, state, city, topic, category, product, uid)

# b_sort = [(country, state, city, topic, category, product),
#           (topic, country, state, category, product),
#           (category, country, product),
#           (product,)]


def read_input(file):
    for line in file:
        yield line.rstrip().split()


def main():
    pt_f = open('partition_lst', 'r')
    boundaries = [line for line in pt_f]
    data = read_input(sys.stdin)
    for e in data:
        for batch in range(batch_number):
            head = "%s|%s" % (
                str(batch), ' '.join(e[i] for i in C[batch][-1]))
            part = bisect_left(boundaries, head) % p
            # batch_head | head_value <TAB> country, ..., product uid
            print "%d\t%s\t%s" % (part, head, ' '.join(e[i] for i in useful))

if __name__ == "__main__":
    main()
