#!/usr/bin/env python
import sys
from collections import Counter


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = read_input(sys.stdin)
    # data = open("batch_map")
    freq = Counter(e[0] for e in data)
    for item in freq:
        print item, ":", freq[item]
    data.close()

if __name__ == "__main__":
    main()
