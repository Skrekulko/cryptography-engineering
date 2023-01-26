# Chapter 9 - Generating Randomness

## Notes

### Something To Think About

***Standard implementation techniques are entirely inadequate to create source code.***

## Exercises

### Exercise 9.1

Investigate the random number generators built into three of your favorite programming languages. Would you use these random number generators for cryptographic purposes?

#### Solution

A very good example is the [random](https://docs.python.org/3/library/random.html) module in Python 3, which is using the [Mersenne Twister PRNG](https://dl.acm.org/doi/10.1145/272991.272995). As it can also be seen in the documentation, it's not cryptographically secure. Check my [Cryptopals Crypto Challenges](https://github.com/Skrekulko/cryptopals-crypto-challenges/tree/main/cryptopals/s03/c23) repo for more details about the possible attacks.

### Exercise 9.2

Using an existing cryptography library, write a short program that generates a 256-bit AES key using a cryptographic *PRNG*.

#### Solution

```python
#! /usr/bin/env python

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main() -> None:
    plaintext = get_random_bytes(16)

    key = get_random_bytes(16)

    iv = get_random_bytes(16)

    print(
        AES.new(key=key, iv=iv, mode=AES.MODE_CBC).encrypt(plaintext).hex(" ")
    )

if __name__ == "__main__":
    main()
```

Output:

```
98 ce f5 f7 9e 9b 34 37 5e c4 8c b7 b2 19 4e c2
```

### Exercise 9.3

For your platform, language, and cryptography library of choice, summarize how the cryptographic prng works internally. Consider issues including but not limited to the following: how the entropy is collected, how reseeding occurs, and how the prng handles reboots.

#### Solution

Please refer to exercise 9.1.

### Exercise 9.4

What are the advantages of using a *PRNG* over an *RNG*? What are the advantages of using an *RNG* over a *PRNG*?

#### Solution

It's an apples and oranges comparison. PRNGs may be ported to other systems and languages. Their implementations are simple to validate. They have a mathematical security specification, and it's simple to create fast PRNGs that empirically fit it (although we don't know how to verify it). RNGs are not portable (they are not totally software anyhow) and significantly more sophisticated (usually, there is a hardware source, checks of that at power-up and in usage, and a conditioning step). It is difficult to persuade a neutral party that a RNG works.

In practice, the best choice is almost always a Cryptographically Strong PRNG, seeded by a public constant when repeatability is desired, or seeded by the output of a RNG (or a secret constant changed manually as needed, perhaps combined with a counter, or time from a truly strictly increasing reference) when repeatability is not desired.

### Exercise 9.5

Using a cryptographic *PRNG* that outputs a stream of bits, implement a random number generator that outputs random integers in the set $0,1,...,n-1$ for any $n$ between 1 and 232.

#### Solution

```python
#! /usr/bin/env python

from Crypto.Random import random


def main() -> None:
    integer = random.getrandbits(32)

    print(integer)

if __name__ == "__main__":
    main()
```

Output:

```
829731937
```

### Exercise 9.6

Implement a naive approach for generating random numbers in the set $0,1,...,191$. For this naive approach, generate a random 8-bit value, interpret that value as an integer, and reduce that value modulo 192. Experimentally generate a large number of random numbers in the set $0,1,...,191$ and report on the distribution of results.

#### Solution

```python
#! /usr/bin/env python

from Crypto.Random import random
from statistics import mean

def main() -> None:
    big_integer = mean([random.getrandbits(32) % 191 for _ in range(1000)])
    small_integer = mean([random.getrandbits(8) % 191 for _ in range(1000)])

    print(big_integer)
    print(small_integer)

if __name__ == "__main__":
    main()
```

Output:

```
95.046
78.821
```

The distribution for large integers is bigger than the distribution for small integers.

### Exercise 9.7

Find a new product or system that uses (or should use) a cryptographic *PRNG*. This might be the same product or system you analyzed for Exercise 1.8. Conduct a security review of that product or system as described in Section 1.12, this time focusing on the issues surrounding the use of random numbers.

#### Solution

Skip.
