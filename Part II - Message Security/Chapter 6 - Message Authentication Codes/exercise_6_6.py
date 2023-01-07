#! /usr/bin/env python

from Crypto.Hash import HMAC, SHA256


def main() -> None:
    plaintext = bytes.fromhex(
        "4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73"
        "65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72"
        "61 70 68 79 21"
    )

    key = bytes.fromhex(
        "0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b"
        "0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b"
    )

    print(HMAC.new(key=key, msg=plaintext, digestmod=SHA256).digest().hex(" "))

if __name__ == "__main__":
    main()
