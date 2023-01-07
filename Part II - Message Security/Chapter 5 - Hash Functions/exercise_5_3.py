#! /usr/bin/env python

import sys
from time import time
from random import randint
from statistics import median
from Crypto.Hash import SHA512


def main() -> None:
    NUMBER_OF_RUNS = 5
    TRUNCATE_SIZES = [8, 16, 24, 32, 40, 48]
    MAX_BIRTHDAY = 48

    for trucate_size in TRUNCATE_SIZES:
        n = 2 ** (MAX_BIRTHDAY // 2)
        run_times = []

        for _ in range(NUMBER_OF_RUNS):
            collisions = {}
            start_time = time()

            for _ in range(0, n + 1):
                random_number = randint(0, n)
                message = random_number.to_bytes((random_number.bit_length() + 7) // 8, sys.byteorder)
                digest = SHA512.new(message).digest()[:trucate_size // 8]

                if digest in collisions and collisions[digest] != message:
                    end_time = time() - start_time
                    run_times.append(end_time)
                    break
                else:
                    collisions[digest] = message

        median_time = median(run_times)
        print(f"SHA-512-{trucate_size}:\t{median_time:0.6f} seconds.")

if __name__ == "__main__":
    main()
