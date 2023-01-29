# Chapter 18 - The Dream of PKI

## Exercises

### Exercise 18.1

Suppose a CA is malicious. What bad things could the CA accomplish?

#### Solution

Issuing fake certificates for public/private key pairs and thus (maliciously) certifies that the public key belongs to some party it's not supposed to belong.

### Exercise 18.2

Assume a universal PKI. Can any security problems arise because of the use of this single PKI across multiple applications?

#### Solution

One disadvantage of multilevel certificates (*certificate chain*) is that the certificates grow larger and require more computations to verify, but this is a relatively small cost in most situations. Another disadvantage is that each extra CA that you add to the system provides another point of attack, and thereby reduces overall system security.

### Exercise 18.3

What policy or organizational challenges might impede or prevent the deployment of a worldwide universal PKI?

#### Solution

Same reason as above, it's just too complicated and there are not enough resources, plus the enormous amount of different points of attack.

### Exercise 18.4

In addition to the examples in Sections 18.2.2–18.2.5, give three example scenarios for which a PKI might be viable.

#### Solution

Skip.
