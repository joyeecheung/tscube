#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

uid = 6
country, state, city = 0, 1, 2
topic, category, product = 3, 4, 5

C = [(
    (country,),
    (country, state),
    (country, state, city),
    (country, state, city, topic),
    (country, state, city, topic, category),
    (country, state, city, topic, category, product)
), (
    (topic,),
    (topic, country),
    (topic, country, state),
    (topic, category, country, state),
    (topic, category, product, country, state)
), (
    (topic, category),
    (topic, category, country),
    (topic, category, product, country)
), (
    (topic, category, product),
)]

head_dict = {
    2: 0,
    5: 1,
    6: 2,
    7: 3
}


index_dict = ("2", "3", "4", "5", "6", "7", "1")


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    #f = open('private_batch_mapped')
    #data = [line for line in read_input(f)]
    data = read_input(sys.stdin)
    # group by batch head
    # e.g. head = "1|2" (country batch, country=2)
    # group = [("1|2", "..... uid"), ("1|2", ".... uid") ....]
    for head, outtergroup in groupby(data, itemgetter(0)):
        batch = int(head.split('|')[0])
        # regions = the batch scheme
        regions = C[batch]
        # area = [(country, state, ...., uid)...]
        area = [e.split() for head, e in outtergroup]
        for R in regions:
            area.sort(key=itemgetter(*R))
            for region, innergroup in groupby(area, itemgetter(*R)):
                if type(region) is str:
                    region = (region,)
                reach = len(set(e[uid] for e in innergroup))
                values = sorted(zip(R, region), key=itemgetter(0))
                indexes = [index_dict[v[0]] for v in values]
                attrs = [v[1] for v in values]
                print "%s|%s\t%s" % (' '.join(indexes), ' '.join(attrs), reach)
if __name__ == "__main__":
    main()
