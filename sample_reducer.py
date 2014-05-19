#!/usr/bin/env python
import sys

p = 4


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = sorted(read_input(sys.stdin))
    count = 0
    for e in data:
        if count == p - 1:
            print e[0]
        count = (count + 1) % p

if __name__ == "__main__":
    main()
