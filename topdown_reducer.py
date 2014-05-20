#!/usr/bin/env python

import sys
from itertools import groupby
from operator import itemgetter

uid = 6
country, state, city = 0, 1, 2
topic, category, product = 3, 4, 5

to_o_index = ("2", "3", "4", "5", "6", "7", "1")

b_hier = [(product, category, topic, city, state, country),
          (product, category, topic),
          (product, category, topic),
          (product, category, topic)]

# b_sort = [(country, state, city, topic, category, product),
#           (topic, country, state, category, product),
#           (category, country, product),
#           (product,)]

# C = [(
#     (country, state, city, topic, category, product),
#     (country, state, city, topic, category),
#     (country, state, city, topic),
#     (country, state, city),
#     (country, state),
#     (country,)
# ), (
#     (country, state, topic, category, product),
#     (country, state, topic, category),
#     (country, state, topic)
# ), (
#     (country, topic, category, product),
#     (country, topic, category),
#     (country, topic)
# ), (
#     (topic, category, product),
#     (topic, category),
#     (topic,)
# )]


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')[1:]

# hierarchy: (product, category, ...) item in b_hier
# region_pos: index in hierarchy denoting current region
# m_value: values of this batch
# m_set: sets of uid


def print_measure(hierarchy, region_pos, m_value, m_set):
    # print "------------------print measure--------------------"
    indexes = sorted(hierarchy[region_pos:])
    print "%s|%s\t%s" % (' '.join(to_o_index[i] for i in indexes),
                         ' '.join(m_value[i] for i in indexes),
                         len(m_set))


def main():
    # f = open('maped')
    # data = sorted([line for line in read_input(f)])
    data = read_input(sys.stdin)

    # initialize
    cur_set = []
    cur_value = []
    cur_b_index = 0  # index in b_hier

    for head, group in groupby(data, itemgetter(0)):
        for pair in group:
            # get 2->0 in "2|1", index in b_hier
            pair_b_index = int(pair[0].split('|')[0])
            # get the tuple
            pair_values = pair[1].split()
            # for 2(country), get the b_hier list (product, ...)
            pair_b_hier = b_hier[pair_b_index]
            pair_b_size = len(pair_b_hier)  # size of the b_hier list

            # print "processing ", pair
            # print "index", pair_b_index
            # print "hierarchy", pair_b_hier

            # initialize, set the first tuple as current
            if not cur_value:
                # print "*" * 15
                # print "First k-v", pair
                # print "*" * 15
                cur_value = list(pair_values)
                cur_set = [set((pair_values[uid],)) for i in pair_b_hier]
                cur_b_index = pair_b_index

            # another batch
            if cur_b_index != pair_b_index:
                # print "*" * 15
                # print "New batch", pair_b_index
                # print "Printing Old batch", cur_b_index
                # print "*" * 15
                print_b_hier = b_hier[cur_b_index]
                print_b_size = len(print_b_hier)
                for print_r_pos in range(print_b_size):
                    print_measure(
                        print_b_hier, print_r_pos, cur_value, cur_set[print_r_pos])
                cur_value = list(pair_values)
                cur_set = [set((pair_values[uid],)) for i in pair_b_hier]
                cur_b_index = pair_b_index
                # print cur_b_index, cur_value, cur_set
                # print "new cur_value", cur_value
                # print "new cur_set", cur_set
                # print "new batch", cur_b_index
                # print "*" * 15

            # watch for changes, output the measure for each group
            for region_pos in range(pair_b_size):
                v_index = pair_b_hier[region_pos]
                # print "waching index\t", v_index
                if pair_values[v_index] != cur_value[v_index]:
                    # print "*" * 15
                    # print "value changed."
                    # print "old value is", v_index, ":", cur_value[v_index], "in ", cur_value
                    # print "new value is", v_index, ":", pair_values[v_index], "in ", pair_values
                    # print "*" * 15
                    print_measure(
                        pair_b_hier, region_pos, cur_value, cur_set[region_pos])
                    cur_set[region_pos].clear()
                    cur_set[region_pos].add(pair_values[uid])
                    cur_value[v_index] = pair_values[v_index]
                    # print "new cur_value", cur_value
                    # print "new cur_set", cur_set
                else:
                    cur_set[region_pos].add(pair_values[uid])
                    # print "*" * 15
                    # print "No change"
                    # print "cur_value", cur_value
                    # print "cur_set", cur_set
                    # print "*" * 15

        # for the last batch
        for region_pos in range(pair_b_size):
            # print "*" * 15
            # print "last batch"
            # print "cur_value", cur_value
            # print "cur_set", cur_set
            print_measure(
                b_hier[cur_b_index], region_pos, cur_value, cur_set[region_pos])

if __name__ == "__main__":
    main()
