# Chapter 6 - Message Authentication Codes

## Notes

### Definitions

- **Definition 8** - *An ideal MAC function is a random mapping from all possible inputs to n-bit outputs.*

- **Definition 9** - *An attack on a MAC is a non-generic method of distinguishing the MAC from an ideal MAC function.*

### Recommended CBC-MAC structure

1. Construct a string $s$ from the concatenation of $l$ and $m$, where $l$ is the length of $m$ encoded in a fixed-length format.

2. Pad $s$ until the length is a multiple of the block size.

3. Apply CBC-MAC to the padded string $s$.

4. Output the last ciphertext block, or part of that block. Do not output any of the intermediate values.

### The Horton Principle

*Authenticate what is meant, not what is said.*

## Exercises

### Exercise 6.1

Describe a realistic system that uses CBC-MAC for message authentication and that is vulnerable to a length extension attack against CBC-MAC.

#### Solution

Skip. (Or just take a look at the [RFC 4493](https://www.rfc-editor.org/rfc/rfc4493).)

### Exercise 6.2

Suppose $c$ is one block long, $a$ and $b$ are strings that are a multiple of the block length, and $M(a\parallel c)=M(b\parallel c)$. Here $M$ is CBC-MAC. Then $M(a\parallel d)=M(b\parallel d)$ for any block $d$. Explain why this claim is true.

#### Solution

```math
M(a)=M(b)\Rightarrow 
\begin{Bmatrix}
M(a\parallel d)=H_{2}=E_{k}(d\oplus H_{1,a})=E_{k}(d\oplus E_{k}(a\oplus IV))
\\ 
M(b\parallel d)=H_{2}=E_{k}(d\oplus H_{1,b})=E_{k}(d\oplus E_{k}(b\oplus IV))
\end{Bmatrix}
M(a\parallel d)=M(b\parallel d)
```

### Exercise 6.3

Suppose $a$ and $b$ are both one block long, and suppose the sender MACs $a$, $b$, and $a\parallel b$ with CBC-MAC. An attacker who intercepts the MAC tags for these messages can now forge the MAC for the message $b\parallel (M(b)\oplus M(a)\oplus b)$, which the sender never sent. The forged tag for this message is equal to $M(a\parallel b)$, the tag for $a\parallel b$. Justify mathematically why this is true.

#### Solution

```math
M[b\parallel M(b)\oplus M(a)\oplus b)]
\Rightarrow 
\begin{Bmatrix}
M(a)=E_{k}(a\oplus IV)
\\ 
M(b)=E_{k}(b\oplus IV)
\end{Bmatrix}
\Rightarrow
E_{k}[(E_k(b\oplus IV)\oplus E_k(a\oplus IV)\oplus b)\oplus E_k(b\oplus IV)]=
E_{k}[b\oplus E_k(a\oplus IV)]=M(a\parallel b)
```

### Exercise 6.4

Suppose message $a$ is one block long. Suppose that an attacker has received the MAC $t$ for $a$ using CBC-MAC under some random key unknown to the attacker. Explain how to forge the MAC for a two-block message of your choice. What is the two-block message that you chose? What is the tag that you chose? Why is your chosen tag a valid tag for your two-block message?

#### Solution

```math
\begin{matrix}
t=M(a)=E_{k}(a\oplus IV)
\\
b\rightarrow M(b)=E_{k}(b\oplus IV)=IV
\\ 
M(b\parallel a)=E_{k}(a\oplus M(b))=E_{k}(a\oplus E_{k}(b\oplus IV))=E_{k}(a\oplus IV)=M(a)=t
\end{matrix}
```

### Exercise 6.5

Using an existing cryptography library, compute the MAC of the message

```
4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73
65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72
61 70 68 79 21 20 20 20 20 20 20 20 20 20 20 20
```

using CBC-MAC with AES and the 256-bit key

```
80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01
```
#### Solution

```python
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
```

Output:

```
c5 57 63 f8 2a cb 32 5c 54 fc fd 87 b6 75 48 96
```

### Exercise 6.6
Using an existing cryptography library, compute the MAC of the message

```
4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73
65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72
61 70 68 79 21
```

using HMAC with SHA-256 and the key

```
0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b
0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b
```

#### Solution

```python
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
```

Output:

```
be 48 c6 59 ee 04 1e dc 12 af 8d 47 96 07 76 18 99 02 e0 11 b1 c6 a5 40 56 a5 b1 0d 96 18 fa 4a
```

### Exercise 6.7

Using an existing cryptography library, compute the MAC of the message

```
4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73
65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72
61 70 68 79 21
```

using GMAC with AES and the 256-bit key

```
80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01
```

and the nonce

```
00 00 00 00 00 00 00 00 00 00 00 01
```

#### Solution

```python
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
```

Output: 

```
e4 1f f7 cf a8 70 ee ff 36 e4 a8 75 ad 5d fb 9c
```
