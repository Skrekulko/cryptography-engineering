#! /usr/bin/env python

from Crypto.Cipher import AES

def main() -> None:
    plaintext = bytes.fromhex(
        "62 6C 6F 63 6B 20 63 69 70 68 65 72 73 20 20 20"
        "68 61 73 68 20 66 75 6E 63 74 69 6F 6E 73 20 78"
        "62 6C 6F 63 6B 20 63 69 70 68 65 72 73 20 20 20"
    )

    key = bytes.fromhex(
        "80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01"
    )

    ciphertext = AES.new(key=key,mode=AES.MODE_ECB).encrypt(plaintext)
    print(ciphertext.hex(" "))

if __name__ == "__main__":
    main()
