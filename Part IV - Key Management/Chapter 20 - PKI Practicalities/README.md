# Chapter 20 - PKI Practicalities

## Exercises

### Exercise 20.1

What fields do you think should appear in a certificate, and why?

#### Solution

Check [X.509](https://www.rfc-editor.org/rfc/rfc5280).

### Exercise 20.2

What are the root SSL keys hard-coded within your Web Browser of choice? When were these keys created? When do they expire?

#### Solution

Skip.

### Exercise 20.3

Suppose you have deployed a PKI, and that the PKI uses certificates in a certain fixed format. You need to update your system. Your updated system needs to be backward compatible with the original version of the PKI and its certificates. But the updated system also needs certificates with extra fields. What problems could arise with this transition? What steps could you have taken when originally designing your system to best prepare for an eventual transition to a new certificate format?

#### Solution

Ugh, feeling tired. Skip.

### Exercise 20.4

Create a self-signed certificate using the cryptography packages or libraries on your machine.

#### Solution

```console
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365
```

### Exercise 20.5

Find a new product or system that uses a PKI. This might be the same product or system that you analyzed for Exercise 1.8. Conduct a security review of that product or system as described in Section 1.12, this time focusing on the security and privacy issues surrounding the use of the PKI.

#### Solution

Skip.
