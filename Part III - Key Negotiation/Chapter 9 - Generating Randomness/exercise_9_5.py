#! /usr/bin/env python

from Crypto.Random import random


def main() -> None:
    integer = random.getrandbits(32)

    print(integer)

if __name__ == "__main__":
    main()
