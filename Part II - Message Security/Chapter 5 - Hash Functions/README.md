# Chapter 5 - Hash Functions

## Notes

### Definitions

- **Definition 4** - *The ideal hash function behaves like a random mapping from all
possible input values to the set of all possible output values.*

- **Definition 5** - *An attack on a hash function is a non-generic method of distinguishing
the hash function from an ideal hash function.*

## Exercises

### Exercise 5.1 - Use a software tool to generate two messages $M$ and $M^{'},M\neq M^{'}$, that produce a collision for MD5. To generate this collision, use one of the known attacks against MD5. A link to example code for finding MD5 collisions is available at: http://www.schneier.com/ce.html.

> [Tunnels in Hash Functions](https://cryptography.hyperlink.cz/MD5_collisions.html "Vlastimil Klima: Tunnels in Hash Functions: MD5 Collisions Within a Minute")

### Exercise 5.2 - Using an existing cryptography library, write a program to compute the SHA-512 hash value of the following message in hex:<br/>&emsp;48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 2E 20 20 20.

> ```python
> #! /usr/bin/env python
>
> from Crypto.Hash import SHA512
> 
> def main() -> None:
>     plaintext = bytes.fromhex(
>         "48 65 6C 6C 6F 2C 20 77 6F 72 6C 64 2E 20 20 20"
>     )
> 
>     print(SHA512.new(plaintext).digest().hex(" "))
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> Output:
> 
> 85 02 7f 3f a3 08 b4 f0 70 b5 66 ca 4d a2 6d af fa 65 d8 61 e6 a2 64 30 d6 9a 5a b7 67 0a 56 f9
> a1 66 8b 80 2e 6d fd 4d dc 99 2b 93 f7 52 f2 9d 76 ce 32 77 7a 32 34 f6 a4 7d b5 aa 4d c5 71 85
> 

### Exercise 5.3 - Consider SHA-512-$n$, a hash function that first runs SHA-512 and then outputs only the first $n$ bits of the result. Write a program that uses a birthday attack to find and output a collision on SHA-512-$n$, where $n$ is a multiple of 8 between 8 and 48. Your program may use an existing cryptography library. Time how long your program takes when $n$ is 8, 16, 24, 32, 40, and 48, averaged over five runs for each n. How long would you expect your program to take for SHA-512-256? For SHA-512-384? For SHA-512 itself?

> ```python
> #! /usr/bin/env python
> 
> import sys
> from time import time
> from random import randint
> from statistics import median
> from Crypto.Hash import SHA512
> 
> 
> def main() -> None:
>     NUMBER_OF_RUNS = 5
>     TRUNCATE_SIZES = [8, 16, 24, 32, 40, 48]
>     MAX_BIRTHDAY = 48
> 
>     for trucate_size in TRUNCATE_SIZES:
>         n = 2 ** (MAX_BIRTHDAY // 2)
>         run_times = []
> 
>         for _ in range(NUMBER_OF_RUNS):
>             collisions = {}
>             start_time = time()
> 
>             for _ in range(0, n + 1):
>                 random_number = randint(0, n)
>                 message = random_number.to_bytes((random_number.bit_length() + 7) // 8, sys.byteorder)
>                 digest = SHA512.new(message).digest()[:trucate_size // 8]
> 
>                 if digest in collisions and collisions[digest] != message:
>                     end_time = time() - start_time
>                     run_times.append(end_time)
>                     break
>                 else:
>                     collisions[digest] = message
> 
>         median_time = median(run_times)
>         print(f"SHA-512-{trucate_size}:\t{median_time:0.6f} seconds.")
> 
> if __name__ == "__main__":
>     main()
> ```
> Output:
> 
> SHA-512-8:      0.000115 seconds.
> 
> SHA-512-16:     0.002221 seconds.
> 
> SHA-512-24:     0.027380 seconds.
> 
> SHA-512-32:     0.698669 seconds.
> 
> SHA-512-40:     10.441236 seconds.
> 
> SHA-512-48:     58.972724 seconds.
> 
> Yeah, for SHA-512 (256, 384, and 512) it'll take some time.

### Exercise 5.4 - Let SHA-512-$n$ be as in the previous exercise. Write a program that finds a message $M$ (a pre-image) that hashes to the following value under SHA-512-8 (in hex):<br/>&emsp;A9.<br/>Write a program that finds a message M that hashes to the following value under SHA-512-16 (in hex):<br/>&emsp;3D 4B.<br/>Write a program that finds a message M that hashes to the following value under SHA-512-24 (in hex):<br/>&emsp;3A 7F 27.<br/>Write a program that finds a message M that hashes to the following value under SHA-512-32 (in hex):<br/>&emsp;C3 C0 35 7C.<br/>Time how long your programs take when n is 8, 16, 24, and 32, averaged over five runs each. Your programs may use an existing cryptography library. How long would you expect a similar program to take for SHA-512-256? For SHA-512-384? For SHA-512 itself?

> ```python
> #! /usr/bin/env python
> 
> import sys
> from time import time
> from random import randint
> from statistics import median
> from Crypto.Hash import SHA512
> 
> 
> def main() -> None:
>     NUMBER_OF_RUNS = 5
>     TRUNCATE_SIZES = [8, 16, 24, 32]
>     DIGESTS = [bytes.fromhex(digest) for digest in ["A9", "3D 4B", "3A 7F 27", "C3 C0 35 7C"]]
>     MAX_BIRTHDAY = 64
> 
>     for (truncate_size, digest) in zip(TRUNCATE_SIZES, DIGESTS):
>         n = 2 ** (MAX_BIRTHDAY // 2)
>         run_times = []
> 
>         for _ in range(NUMBER_OF_RUNS):
>             start_time = time()
> 
>             for _ in range(0, n + 1):
>                 random_number = randint(0, n)
>                 random_message = random_number.to_bytes((random_number.bit_length() + 7) // 8, sys.byteorder)
>                 random_digest = SHA512.new(random_message).digest()[:truncate_size // 8]
> 
>                 if random_digest == digest:
>                     end_time = time() - start_time
>                     run_times.append(end_time)
>                     break
> 
>         median_time = median(run_times)
>         print(f"SHA-512-{truncate_size}:\t{median_time:0.6f} seconds.")
> 
> if __name__ == "__main__":
>     main()
> ```
> 
> Output:
> 
> SHA-512-8:      0.002076 seconds.
> 
> SHA-512-16:     0.404807 seconds.
> 
> SHA-512-32:     196.301877 seconds.
> 
> The others took way too much time...

### Exercise 5.5 - In Section 5.2.1, we claimed that $m$ and $m^{'}$ both hash to $H\_{2}$. Show why this claim is true.

> Let hash function be $H_{k}=AES_k(H_{i-1}\bigoplus m_{i})$, where $H_{0}$ is a 128-bit block of all zeros, and message $m$ is split into 128-bit blocks $m_{1},...,m_{k}$, the padding scheme is not important. The hash function is built from AES with 256-bit key, and the key being set to all zeros.
> 
> Let message $m^{'}$:
> 
> ```math
> m^{'}\left\{\begin{matrix}
> m^{'}_{1}=m_{2}\bigoplus H_{1}
> \\ 
> m^{'}_{2}=H_{2}\bigoplus m_{2}\bigoplus H_{1}
> \end{matrix}\right.
> ```
> After doing some basic math we get the result we want:
> 
> ```math
> \begin{matrix}
> H^{'}_{1}=AES_k(H_{0}\bigoplus m^{'}_{1})=AES_k(H_{0}\bigoplus m_{2}\bigoplus H_{1})=AES_k(m_{2}\bigoplus H_{1})=H_{2}
> \\ 
> H^{'}_{2}=AES_k(H^{'}_{1}\bigoplus m^{'}_{2})=AES_k(H_{2}\bigoplus H_{2}\bigoplus m_{2}\bigoplus H_{1})=AES_k(m_{2}\bigoplus H_{1})=H_{2}
> \end{matrix}
> ```
> 

### Exercise 5.6 - Pick two of the SHA-3 candidate hash function submissions and compare their performance and their security under the currently best published attacks. Information about the SHA-3 candidates is available at http://www.schneier.com/ce.html.

> Check this [paper](https://ieeexplore.ieee.org/abstract/document/6516382) about SHA-3 candidates and their comparison.
