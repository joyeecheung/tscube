#!/usr/bin/env python
import sys
from itertools import product


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')

def main():
    data = read_input(sys.stdin)
    for e in data:
        print '\t'.join(e)

if __name__ == "__main__":
    main()
