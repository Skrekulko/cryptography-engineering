#! /usr/bin/env python

from Crypto.Cipher import AES

def main() -> None:
    plaintext = bytes.fromhex(
        "29 6C 93 FD F4 99 AA EB 41 94 BA BC 2E 63 56 1D"
    )

    key = bytes.fromhex(
        "80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01"
    )

    ciphertext = AES.new(key=key,mode=AES.MODE_ECB).encrypt(plaintext)
    print(ciphertext.hex(" "))

if __name__ == "__main__":
    main()