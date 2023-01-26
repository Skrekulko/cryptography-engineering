# Chapter 7 - The Secure Channel

## Exercises

### Exercise 7.1

In our design of a secure channel, we said that the message numbers must not repeat. What bad things can happen if the message numbers do repeat?

#### Solution

Since the numbers also serve as IVs, the same IV could be used twice, which is a security issue. Not only that, but duplicate numbers would desynchronize the order of the messages, thus rendering their reconstruction meaningless.

### Exercise 7.2

Modify the algorithms for the secure channel in this chapter to use the encrypt-then-authenticate order for encryption and authentication.

#### Solution

The state algorithm stays the same, but the algorithm for sending and receiving a message is modified, by encrypting first and then authenticating. Nothing hard, but going to skip this one by not actually writing it down.

### Exercise 7.3

Modify the algorithms for the secure channel in this chapter to use the a dedicated, single-key mode for providing both encryption and authentication. You can use OCB, CCM, CWC, or GCM as a black box.

#### Solution

The state algorithm stays the same, and the algorithm for sending and receiving a message is actually a black box since the listed modes provide both encryption and authentication at the same time. Same as before, not going to bother writing this one down. For more information, check NIST publications.

### Exercise 7.4

Compare and contrast the advantages and disadvantages among the different orders of applying encryption and authentication when creating a secure channel.

#### Solution

Already explained in the book. Skip.

### Exercise 7.5

Find a new product or system that uses (or should use) a secure channel. This might be the same product or system you analyzed for Exercise 1.8. Conduct a security review of that product or system as described in Section 1.12, this time focusing on the security and privacy issues surrounding the secure channel.

#### Solution

Skip.

### Exercise 7.6

Suppose Alice and Bob are communicating using the secure channel described in this chapter. Eve is eavesdropping on the communications. What types of traffic analysis information could Eve learn by eavesdropping on the encrypted channel? Describe a situation in which information exposure via traffic analysis is a serious privacy problem.

#### Solution

Eva does not lear anything about the messages, except for their timing and size. Given that Eve can see the size and timing of messages on a communication channel, she can find out who is communicating with whom, how much, and when.
