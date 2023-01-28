# Chapter 12 - RSA

## Exercises

### Exercise 12.1

Let $p = 89$, $q = 107$, $n = pq$, $a = 3$, and $b = 5$. Find $x$ in $\mathbb{Z}_{n}$ such that $a = x \bmod p$ and $b = x \bmod q$.

#### Solution

```math
\begin{matrix}
\textrm{Garner's Formula: }x=\left [ \left [ (a-b)(q^{-1}\bmod p) \right ] \bmod p\right ]\cdot q + b\\\
\\
\begin{aligned}
\Rightarrow x
&=\left [ \left [ (3-5)(5\bmod 89) \right ] \bmod 89\right ]\cdot 107 + 5\\
&=\left [ \left [ (-2)(5) \right ] \bmod 89\right ]\cdot 107 + 5\\
&=\left [ 10 \bmod 89\right ]\cdot 107 + 5\\
&=10\cdot 107 + 5\\
&=\underline{8458}
\end{aligned}\\\
\\
a\equiv x\bmod p\Rightarrow 3\equiv 8458\equiv 3\bmod 89
\\
b\equiv x\bmod q\Rightarrow 5\equiv 8458\equiv 5\bmod 107
\end{matrix}
```

### Exercise 12.2

Let $p = 89$, $q = 107$, $n = pq$, $x = 1796$, and $y = 8931$. Compute $x + y \bmod n$ directly. Compute $x + y \bmod n$ using CRT representations.

#### Solution

```math
\begin{matrix}
\textrm{Directly:}
\\ 
x+y\bmod n\Rightarrow 1796+8931\equiv 10727\equiv 1204\bmod 9523
\\\\\
\textrm{CRT}:
\\
x+y\bmod n
\left\{\begin{matrix}
x+y\equiv a_{1}\bmod p\Rightarrow a_{1}\equiv 10727\equiv 47\bmod 89
\\
x+y\equiv a_{2}\bmod q\Rightarrow a_{2}\equiv 10727\equiv 27\bmod107
\end{matrix}\right.
\\
xy=a_{1}m_{2}q+a_{2}m_{1}p=47\cdot 5\cdot 107+27\cdot (-6)\cdot 89=\underline{10727}
\\\\
\textrm{(The integers }m_{1}\textrm{ and }m_{2}\textrm{ are computed with the Extended Euclidean Algorithm.)}
\end{matrix}
```

### Exercise 12.3

Let $p = 89$, $q = 107$, $n = pq$, $x = 1796$, and $y = 8931$. Compute $xy \bmod n$ directly. Compute $xy \bmod n$ using CRT representations.

#### Solution

```math
\begin{matrix}
\textrm{Directly:}
\\ 
xy\bmod n\Rightarrow 1796\cdot8931\equiv 16040076\equiv 3344\bmod 9523
\\\\\
\textrm{CRT}:
\\
xy\bmod n
\left\{\begin{matrix}
xy\equiv a_{1}\bmod p\Rightarrow a_{1}\equiv 3344\equiv 51\bmod 89
\\
xy\equiv a_{2}\bmod q\Rightarrow a_{2}\equiv 3344\equiv 27\bmod107
\end{matrix}\right.
\\
xy=a_{1}m_{2}q+a_{2}m_{1}p=51\cdot 5\cdot 107+27\cdot (-6)\cdot 89=12867\bmod 9523=\underline{3344}
\\\\
\textrm{(The integers }m_{1}\textrm{ and }m_{2}\textrm{ are computed with the Extended Euclidean Algorithm.)}
\end{matrix}
```

### Exercise 12.4

Let $p = 83$, $q = 101$, $n = pq$, and $e = 3$. Is $(n, e)$ a valid RSA public key? If so, compute the corresponding private RSA key $d$. If not, why not?

#### Solution

```math
\begin{matrix}
n=pq=83\cdot 101=8383\\
\\
\textrm{We'll use Eurler's totient function instead of Carmichael's:}\\
\phi (n)=(p-1)(q-1)=(83-1)(101-1)=82\cdot 100=8200\\
\\
\textrm{Choose $e$ such that $1 < e < \phi (n)$ and is coprime to $\phi (n)$.}\\
e=3\\
\\
\textrm{Calculate }d\textrm{, themodular multiplicative inverse of }e\bmod \phi (n)\textrm{.}\\
d\equiv e^{-1}\equiv \underline{5467}\bmod 8383
\end{matrix}
```

### Exercise 12.5

Let $p = 79$, $q = 89$, $n = pq$, and $e = 3$. Is $(n, e)$ a valid RSA public key? If so, compute the corresponding private RSA key $d$. If not, why not?

#### Solution

```math
\begin{matrix}
n=pq=73\cdot 89=6497\\
\\
\textrm{We'll use Eurler's totient function instead of Carmichael's:}\\
\phi (n)=(p-1)(q-1)=(73-1)(89-1)=72\cdot 88=6336\\
\\
\textrm{Choose $e$ such that $ 1 < e < \phi (n) $ and is coprime to $\phi (n)$.}\\
e=3\textrm{ is not a coprime to }\phi (n)\textrm{, since gcd}(e, \phi (n))=3\neq 1
\end{matrix}
```

### Exercise 12.6

To speed up decryption, Alice has chosen to set her private key $d = 3$ and computes e as the inverse of $d$ modulo $t$. Is this a good design decision?

#### Solution

The main cost for a user of RSA is computing modular exponentiation, which for the exponent $x$ costs $\left \lfloor \log _{2}x \right \rfloor$ squarings and $H(x)-1$ multiplications, where $H$ is Hamming weight. The most efficient exponent is $3$, but this can be only done for the public exponent. If picked as a private exponent $d=3$, $e$ would still have to be published in order for anyone to encrypt messages, but by doing this, then armed with knowledge of $e$ and $d$, $\lambda (n)$ and factor $n$ it is possible to find and break the whole RSA. What if $d$ would be picked to be small to speed up decryption? As it happens, if $d$ is merely smaller than about $\sqrt[4]{n}$, [Wiener's attack](https://en.wikipedia.org/wiki/Wiener%27s_attack) or a variant thereof can be used to recover it. It is therefore crucial that the private exponent $d$ be near uniformly distributed in the whole possible space, which is effectively the case even if the public exponent $e$ is chosen always to be something small like $3$ or $65537$. Thus while it is perfectly safe in sensible RSA-type cryptosystem to always use $e=3$, it is dangerous to choose even moderately small $d$; the exponents are very much not interchangeable.

### Exercise 12.7

Does a 256-bit RSA key (a key with a 256-bit modulus) provide strength similar to that of a 256-bit AES key?

#### Solution

Hell nah! [NIST recommends](https://csrc.nist.gov/publications/detail/sp/800-131a/rev-2/final) a *minimum* of 2048-bit keys for RSA.

### Exercise 12.8

Let $p = 71$, $q = 89$, $n = pq$, and $e = 3$. First find $d$. Then compute the signature on $m_{1} = 5416$, $m_{2} = 2397$, and $m_{3} = m_{1}m_{2} \bmod n$ using the basic RSA operation. Show that the third signature is equivalent to the product of the first two signatures.

#### Solution

```math
\begin{matrix}
n=pq=71\cdot 89=\underline{6319}
\\
\phi (n)=(p-1)(q-1)=(71-1)(89-1)=70\cdot 88=\underline{6160}
\\
d\equiv e^{-1}\bmod \phi (n)\equiv \underline{4107}
\\
s_{1}\equiv m_{1}^{e}\bmod n \equiv \underline{829}
\\
s_{2}\equiv m_{2}^{e}\bmod n \equiv \underline{2187}
\\
s_{3}\equiv m_{3}^{e}\equiv (m_{1}m_{2})^{e}\bmod n \equiv \underline{8789}
\\
\underline{s_{12}\equiv s_{1}s_{2}\equiv m_{1}^{e}m_{2}^{e}\equiv (m_{1}m_{2})^{e}\equiv m_{3}^{e}\equiv s_{3}}\bmod n
\end{matrix}
```
