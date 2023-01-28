# Chapter 14 - Key Negotiation

## Exercises

### Exercise 14.1

In Section 14.5, we stated that a property of the protocol could result in providing erroneous information to investigating administrators. Give a concrete scenario where this could be a problem.

#### Solution

```math
\begin{matrix}
\textbf{ALICE} &  & \textbf{BOB}
\\
\textrm{Choose suitable $(p,q,g)$}
\\
x\in _{R}{\{1,...,q-1\}}
\\
& (p,q,g),X:=g^{x},
\\
& \overset{\textrm{AUTH$_{A}$}}{\longrightarrow}
\\
& & \textrm{Check $(p,q,g)$, $X$, AUTH$_{A}$}
\\
& & y\in _{R}{\{1,...,q-1\}}
\\
& Y:=g^{y}
\\
& \overset{\textrm{AUTH$_{B}$}}{\longleftarrow}
\\
\textrm{Check $Y$, AUTH$_{B}$}
\\
k\leftarrow Y^{x} & & k\leftarrow X^{y}
\end{matrix}
```

The mentioned property of the protocol is the *lack of "liveness"*, since one party cannot (in this case Bob) cannot be sure, if the other party (Alice) is "alive" and that it's not talking to a replaying ghost. This means, that we'll be replying to a "dead" party and we wouldn't even know it.

### Exercise 14.2

Suppose Alice and Bob implement the final protocol in Section 14.7. Could an attacker exploit a property of this protocol to mount a denial-of-service attack against Alice? Against Bob?

#### Solution

```math
\begin{matrix}
\textbf{ALICE} &  & \textbf{BOB}
\\
\textrm{$s\leftarrow$ min $p$ size}
\\
N_{a}\in _{R}{\{0,...,2^{256}-1\}}
\\
& \overset{s,N_{a}}{\longrightarrow}
\\
& & \textrm{Choose $(p,q,g)$}
\\
& & x\in _{R}{\{1,...,q-1\}}
\\
& (p,q,g),X:=g^{x},
\\
& \overset{\textrm{AUTH$_{B}$}}{\longleftarrow}
\\
\textrm{Check $(p,q,g)$, $X$, AUTH$_{B}$}
\\
y\in _{R}{\{1,...,q-1\}}
\\
& \overset{\textrm{$Y:=g^{y}$, AUTH$_{A}$}}{\longrightarrow}
\\
& & \textrm{Check $Y$, AUTH$_{A}$}
\\
\textrm{$k \leftarrow $ SHA$_{d}$-256($X^{y}$)} & & \textrm{$k \leftarrow $ SHA$_{d}$-256($Y^{x}$)}
\end{matrix}
```

If I understand it correctly, the denial-of-service attack could happen when Bob awaits authentication from Alice. An attack could make thousands of such connections and just let Bob hang on the authentication part from Alice. He would be waiting for an authentication with no result.

### Exercise 14.3

Find a new product or system that uses (or should use) a key negotiation protocol. This might be the same product or system you analyzed for Exercise 1.8. Conduct a security review of that product or system as described in Section 1.12, this time focusing on the security and privacy issues surrounding the key negotiation protocol.

#### Solution

I refuse to write down this kind of exercises. Skip.
