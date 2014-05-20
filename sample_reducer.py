#!/usr/bin/env python
import sys

p = 4


def read_input(file):
    for line in file:
        yield line.rstrip().split('\t')


def main():
    data = sorted(read_input(sys.stdin))
    sample_size = len(data)
    for i in range(0, sample_size, sample_size/p):
        print data[i][0]

if __name__ == "__main__":
    main()
