#! /usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main() -> None:
    plaintext = get_random_bytes(16)

    key = get_random_bytes(16)

    iv = get_random_bytes(16)

    print(
        AES.new(key=key, iv=iv, mode=AES.MODE_CBC).encrypt(plaintext).hex(" ")
    )

if __name__ == "__main__":
    main()
