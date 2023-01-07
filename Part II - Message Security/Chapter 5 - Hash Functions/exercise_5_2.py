#! /usr/bin/env python

from Crypto.Hash import SHA512

def main() -> None:
    plaintext = bytes.fromhex(
        "48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 2E 20 20 20"
    )

    print(SHA512.new(plaintext).digest().hex(" "))

if __name__ == "__main__":
    main()
