#! /usr/bin/env python

from Crypto.Cipher import DES


def complement(byte_string: bytes) -> bytes:
    return bytes((byte ^ 0xFF) for byte in byte_string)


def main() -> None:
    key = bytes.fromhex("0102030405060708")
    plaintext = bytes.fromhex("1020304050607080")
    ciphertext = DES.new(key=key,mode=DES.MODE_ECB).encrypt(plaintext)

    complementKey = complement(key)
    complementPlaintext = complement(plaintext)
    complementCiphertext = DES.new(key=complementKey,mode=DES.MODE_ECB).encrypt(complementPlaintext)

    assert complement(ciphertext) == complementCiphertext

if __name__ == "__main__":
    main()