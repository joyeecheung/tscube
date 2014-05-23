#!/usr/bin/env python
import sys

p = 4

def read_input(file):
    for line in file:
        yield line.rstrip()


def main():
    data = sorted(read_input(sys.stdin))
    sample_size = len(data)
    for i in range(sample_size/p, sample_size, sample_size/p):
        print data[i]

if __name__ == "__main__":
    main()
