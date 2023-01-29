# Chapter 21 - Storing Secrets

## Exercises

### Exercise 21.1

Investigate how login passwords are stored on your machine. Write a program that, given a stored (encrypted or hashed) password, exhaustively searches for the real password. How long would it take your program to exhaustively search through the top one million passwords?

#### Solution

Although most of us probably already know this, for new comers, please see this [article](https://tldp.org/HOWTO/User-Authentication-HOWTO/x71.html) on how the user information is stored on Linux. Not writing a program for this exercise. (Partial skip?)

### Exercise 21.2

Investigate how private keys are stored with GNU Privacy Guard (GPG). Write a program that, given a stored encrypted GPG private key, exhaustively searches for the password and recovers the private key. How long would it take your program to exhaustively search through the top one million passwords?

#### Solution

According to the [GNU Privacy Handbook](https://www.gnupg.org/gph/en/manual/c481.html): *GnuPG does not store your raw private key on disk. Instead it encrypts it using a symmetric encryption algorithm. That is why you need a passphrase to access the key. Thus there are two barriers an attacker must cross to access your private key: (1) he must actually acquire the key, and (2) he must get past the encryption.*

### Exercise 21.3

Consider a 24-bit salt. Given a group of 64 users, would you expect two users to have the same salt? 1024 users? 4096 users? 16,777,216 users?

#### Solution

To summarize it quickly: *a lot*. Check this [answer](https://security.stackexchange.com/questions/10659/general-purpose-slow-unique-hash-routine-for-dup-checking-of-private-data-witho/10661#10661) on Stack Exchange.

### Exercise 21.4

Find a new product or system that maintains long-term secrets. This might be the same product or system you analyzed for Exercise 1.8. Conduct a security review of that product or system as described in Section 1.12, this time focusing on issues surrounding how the system might store these secrets.

#### Solution

Skip.
