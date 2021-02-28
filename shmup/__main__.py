#!/usr/bin/env python3

import sys

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Hello")

if __name__ == '__main__':
    sys.exit(main())