#! /usr/bin/env python

from Crypto.Random import random
from statistics import mean

def main() -> None:
    big_integer = mean([random.getrandbits(32) % 191 for _ in range(1000)])
    small_integer = mean([random.getrandbits(8) % 191 for _ in range(1000)])

    print(big_integer)
    print(small_integer)

if __name__ == "__main__":
    main()
