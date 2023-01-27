#! /usr/bin/env python

from random import randint
from math import log2, floor
from Crypto.Util.number import isPrime

def main() -> None:
    l = 2**255
    u = 2**256 - 1

    assert 2 < l <= u

    r = 100 * floor(log2(3) + 1)

    for i in range(r, 0, -1):
        n = randint(l, u)

        assert n > 3

        if isPrime(n):
            print(n)
            break


if __name__ == "__main__":
    main()
