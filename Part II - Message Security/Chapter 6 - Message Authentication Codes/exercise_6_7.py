#! /usr/bin/env python

from Crypto.Cipher import AES


def main() -> None:
    plaintext = bytes.fromhex(
        "4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73"
        "65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72"
        "61 70 68 79 21"
    )

    key = bytes.fromhex(
        "80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01"
    )

    nonce = bytes.fromhex(
        "00 00 00 00 00 00 00 00 00 00 00 01"
    )

    print(
        AES.new(key=key, nonce=nonce, mode=AES.MODE_GCM).encrypt_and_digest(plaintext)[1].hex(" ")
    )

if __name__ == "__main__":
    main()
