#! /usr/bin/env python

from Crypto.Cipher import AES

def main() -> None:
    iv = bytes.fromhex(
        "87 F3 48 FF 79 B8 11 AF 38 57 D6 71 8E 5F 0F 91"
    )

    plaintext = bytes.fromhex(
        "7C 3D 26 F7 73 77 63 5A 5E 43 E9 B5 CC 5D 05 92"
        "6E 26 FF C5 22 0D C7 D4 05 F1 70 86 70 E6 E0 17"
    )

    key = bytes.fromhex(
        "80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
        "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01"
    )

    ciphertext = AES.new(key=key,mode=AES.MODE_CBC,iv=iv).encrypt(plaintext)
    print(ciphertext.hex(" "))

if __name__ == "__main__":
    main()
