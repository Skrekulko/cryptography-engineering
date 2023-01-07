#! /usr/bin/env python

import sys
from time import time
from random import randint
from statistics import median
from Crypto.Hash import SHA512


def main() -> None:
    NUMBER_OF_RUNS = 5
    TRUNCATE_SIZES = [8, 16, 24, 32]
    DIGESTS = [bytes.fromhex(digest) for digest in ["A9", "3D 4B", "3A 7F 27", "C3 C0 35 7C"]]
    MAX_BIRTHDAY = 64

    for (truncate_size, digest) in zip(TRUNCATE_SIZES, DIGESTS):
        n = 2 ** (MAX_BIRTHDAY // 2)
        run_times = []

        for _ in range(NUMBER_OF_RUNS):
            start_time = time()

            for _ in range(0, n + 1):
                random_number = randint(0, n)
                random_message = random_number.to_bytes((random_number.bit_length() + 7) // 8, sys.byteorder)
                random_digest = SHA512.new(random_message).digest()[:truncate_size // 8]

                if random_digest == digest:
                    end_time = time() - start_time
                    run_times.append(end_time)
                    break

        median_time = median(run_times)
        print(f"SHA-512-{truncate_size}:\t{median_time:0.6f} seconds.")

if __name__ == "__main__":
    main()
