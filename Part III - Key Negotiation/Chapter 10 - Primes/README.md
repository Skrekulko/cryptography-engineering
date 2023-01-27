# Chapter 10 - Primes

## Notes

### Lemmas And Theorems

**Lemma 1** - $\textit{If a | b and b | c then a | c.}$

*Proof*. If $a\\, |\\, b$, then there is an integer s such that $as=b$. (After all, $b$ is divisible by a so it must be a multiple of $a$.) And if $b\\, |\\, c$ then there is an integer $t$ such that $bt=c$. But this implies that $c=bt=(as)t=a(st)$ and therefore $a$ is a divisor of $c$. (To follow this argument, just verify that each of the equal signs is correct. The conclusion is that the first item $c$ must be equal to the last item $a(st)$.)

**Lemma 2** - $\textit{Let n be a positive number greater than 1. Let d be the smallest divisor of n that is greater than 1. Then d is prime.}$

*Proof*. First of all, we have to check that $d$ is well defined. (If there is a number $n$ that has no smallest divisor, then $d$ is not properly defined and the lemma is nonsensical.) We know that $n$ is a divisor of $n$, and $n > 1$, so there is at least one divisor of $n$ that is greater than $1$. Therefore, there must also be a smallest divisor greater than $1$.

To prove that $d$ is prime, we use a standard mathematician’s trick called *reductio ad absurdum* or *proof by contradiction*. To prove a statement $X$, we first assume that $X$ is not true and show that this assumption leads to a contradiction. If assuming that $X$ is not true leads to a contradiction, then obviously $X$ must be true.

In our case, we will assume that $d$ is not a prime. If $d$ is not a prime, it has a divisor $e$ such that $1 < e < d$. But we know from **Lemma 1** that if $e\\, |\\, d$ and $d\\, |\\, n$ then $e\\, |\\, n$, so $e$ is a divisor of $n$ and is smaller than $d$. But this is a contradiction, because $d$ was defined as the smallest divisor of $n$. Because a contradiction cannot be true, our assumption must be false, and therefore $d$ must be prime.

**Theomer 3** (Euclid) - $\textit{There are an infinite number of primes.}$

*Proof*. We again assume the opposite of what we try to prove. Here we assume that the number of primes is finite, and therefore that the list of primes is finite. Let’s call them $p_{1},p_{2},p_{3},...,p_{k}$, where $k$ is the number of primes. We define the number $n:=p_{1},p_{2},p_{3},...,p_{k+1}$, which is the product of all our primes plus one.

Consider the smallest divisor greater than $1$ of $n$; we’ll call it $d$ again. Now $d$ is prime (by **Lemma 2**) and $d\\, |\\, n$. But none of the primes in our finite list of primes is a divisor of $n$. After all, they are all divisors of $n − 1$, so if you divide $n$ by one of the $p_{i}$’s in the list, you are always left with a remainder of $1$. So $d$ is a prime and it is not in the list. But this is a contradiction, as the list is defined to contain all the primes. Thus, assuming that the number of primes is finite leads to a contradiction. We are left to conclude that the number of primes is infinite.

## Exercises

### Exercise 10.1

Implement **SmallPrimeList**. What is the worst-case performance of **SmallPrimeList**? Generate a graph of the timings for your implementation and $n=2,4,8,16,...,2^{20}$.

#### Solution



### Exercise 10.2

Compute $13635+16060+8190+21363\bmod 29101$ in two ways and verify the equivalence: by reducing modulo $29101$ after each addition and by computing the entire sum first and then reducing modulo $29101$.

#### Solution

```math
\begin{matrix}
(13635+16060)+8190+21363\equiv (594+8190)+21363\equiv (8784+21363)\equiv 1046\bmod 29101
\\ 
13635+16060+8190+21363\equiv 59248\equiv 1046\bmod 29101
\end{matrix}
```

### Exercise 10.3

Compute the result of $12358\cdot 1854\cdot 14303\bmod 29101$ in two ways and verify the equivalence: by reducing modulo $29101$ after each multiplication and by computing the entire product first and then reducing modulo $29101$.

#### Solution

```math
\begin{matrix}
(12358\cdot 1854)\cdot 14303\equiv (9245\cdot 14303)\equiv 25392\bmod 29101
\\ 
12358\cdot 1854\cdot 14303\equiv 327706502796\equiv 25392\bmod 29101
\end{matrix}
```

### Exercise 10.4

Is $\\{1,3,4\\}$ a subgroup of the multiplicative group of integers modulo $7$?

#### Solution

```math
\begin{matrix}
\textrm{If you multiply any two elements from the same subgroup modulo $7$, you get another element from that subgroup.}\\\
\\
1\cdot 3\equiv 3\bmod 7\in \left \{ 1,3,4 \right \}
\\
1\cdot 4\equiv 4\bmod 7\in \left \{ 1,3,4 \right \}
\\
3\cdot 4\equiv 5\bmod 7\notin \left \{ 1,3,4 \right \}\\\
\\
\left \{ 1,3,4 \right \}\textrm{is not a subgroup of }\mathbb{Z}^{*}_{7}.
\end{matrix}
```

### Exercise 10.5

Use the **GCD** algorithm to compute the GCD of $91261$ and $117035$.

#### Solution

```math
\begin{aligned}
\textrm{gcd}(91261,117035)
&\rightarrow \textrm{gcd}(91261,117035)\\
&\rightarrow \textrm{gcd}(25774,91261)\\
&\rightarrow \textrm{gcd}(13939,25774)\\
&\rightarrow \textrm{gcd}(11835,13939)\\
&\rightarrow \textrm{gcd}(2104,11835)\\
&\rightarrow \textrm{gcd}(1315,2104)\\
&\rightarrow \textrm{gcd}(789,1315)\\
&\rightarrow \textrm{gcd}(526,789)\\
&\rightarrow \textrm{gcd}(263,526)\\
&\rightarrow \textrm{gcd}(263,263)\\
&\rightarrow \textrm{gcd}(0,263)\Rightarrow \textrm{gcd}(91261,117035)=263
\end{aligned}
```

### Exercise 10.6

Use the **ExtendedGCD** algorithm to compute the inverse of $74$ modulo the prime $167$.

#### Solution

```math
\begin{matrix}

\begin{array}{cccc}
167=74(2)+19 & | & 19=167-74(2)
\\
74=19(3)+17 & | & 17=74-19(3)
\\
19=17+2 & | & 2=19-17
\\
17=2(8)+1 & | & 1=17-2(8)
\\
2=1(2)+0 & |
\end{array}\\\

\\ 

\begin{aligned}
1
&=17-2(8)\\
&=\left [ 74-19(3) \right ]-(19-17)(8)=74-19(3)-19(8)+17(8)=74-19(11)+17(8)\\
&=74-\left [ 167-74(2) \right ](11)+\left [ 74-19(3) \right ](8)=74-167(11)+74(22)+74(8)-19(24)=74(31)-167(11)-19(24)\\
&=74(31)-167(11)-\left [ 167-74(2) \right ](24)=74(31)-167(11)-167(24)+74(48)=\underline{74(79)}-167(35)
\end{aligned}\\\

\\ 

1=74(79)-167(35)\Rightarrow \underline{74\cdot 79\equiv 5846\equiv 1\bmod 167}

\end{matrix}
```

### Exercise 10.7

Implement **GenerateLargePrime** using a language or library that supports big integers. Generate a prime within the range $l=2^{255}$ and $u=2^{256}-1$.

#### Solution

```python
#! /usr/bin/env python

from random import randint
from math import log2, floor
from Crypto.Util.number import isPrime

def main() -> None:
    l = 2**255
    u = 2**256 - 1

    assert 2 < l <= u

    r = 100 * floor(log2(3) + 1)

    for i in range(r, 0, -1):
        n = randint(l, u)

        if isPrime(n):
            print(n)
            break


if __name__ == "__main__":
    main()
```

Output:

```
109671822172682122660803926066174899969085505182505003409826127303573265703833
```

### Exercise 10.8

Give pseudocode for the exponentiation routine described in Section 10.4.2. Your pseudocode should not be recursive but should instead use a loop.

#### Solution

```python
def BinaryAlgorithm(a, s, n):
    a %= n
    for _ in range(s):
        a = a ** 2 % n
    return a
```

### Exercise 10.9

Compute $27^{35}\bmod 569$ using the exponentiation routine described in Section 10.4.2. How many multiplications did you have to perform?

#### Solution

```python
#! /usr/bin/env python

def BinaryAlgorithm(a, s, n):
    a %= n
    for i in range(s):
        a = a ** 2 % n
    return a, i + 1

def main() -> None:
    a = 27
    s = 35
    n = 569

    result = BinaryAlgorithm(a, s, n)
    print(f"The result is {result[0]} with {result[1]} multiplications done.")


if __name__ == "__main__":
    main()
```

Output:

```
The result is 345 with 35 multiplications done.
```
