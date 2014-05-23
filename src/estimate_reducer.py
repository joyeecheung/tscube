#!/usr/bin/env python
import sys

p = 3

def read_input(file):
    for line in file:
        yield line.rstrip()


def main():
    data = sorted(read_input(sys.stdin))
    size = len(data)
    for i in range(size/p, size - size/p + 1, size/p):
        print data[i]

if __name__ == "__main__":
    main()
