#! /usr/bin/env python

from Crypto.Cipher import AES

def main() -> None:
    ciphertext = bytes.fromhex(
        "53 9B 33 3B 39 70 6D 14 90 28 CF E1 D9 D4 A4 07"
    )

    key = bytes.fromhex(
        "80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01"
    )

    plaintext = AES.new(key=key,mode=AES.MODE_ECB).decrypt(ciphertext)
    print(plaintext.hex(" "))

if __name__ == "__main__":
    main()