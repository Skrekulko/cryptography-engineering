# Chapter 6 - Message Authentication Codes

## Exercises

### Exercise 6.1 - Describe a realistic system that uses CBC-MAC for message authentication and that is vulnerable to a length extension attack against CBC-MAC.

> 

### Exercise 6.2 -Suppose c is one block long, a and b are strings that are a multiple of the block length, and $M(a\parallel c)=M(b\parallel c)$. Here $M$ is CBC-MAC. Then $M(a\parallel d)=M(b\parallel d)$ for any block $d$. Explain why this claim is true.

> 

### Exercise 6.3 - Suppose $a$ and $b$ are both one block long, and suppose the sender MACs $a$, $b$, and $a\parallel b$ with CBC-MAC. An attacker who intercepts the MAC tags for these messages can now forge the MAC for the message $b\parallel (M(b)\bigoplus M(a)\bigoplus b)$, which the sender never sent. The forged tag for this message is equal to $M(a\parallel b)$, the tag for $a\parallel b$. Justify mathematically why this is true.

> 

### Exercise 6.4 - Suppose message a is one block long. Suppose that an attacker has received the MAC $t$ for $a$ using CBC-MAC under some random key unknown to the attacker. Explain how to forge the MAC for a two-block message of your choice. What is the two-block message that you chose? What is the tag that you chose? Why is your chosen tag a valid tag for your two-block message?

> 

### Exercise 6.5 - Using an existing cryptography library, compute the MAC of the message<br/>&emsp;4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73<br/>&emsp;65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72<br/>&emsp;61 70 68 79 21 20 20 20 20 20 20 20 20 20 20 20<br/>using CBC-MAC with AES and the 256-bit key<br/>&emsp;80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00<br/>&emsp;00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01.

> 

### Exercise 6.6 - Using an existing cryptography library, compute the MAC of the message<br/>&emsp;4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73<br/>&emsp;65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72<br/>&emsp;61 70 68 79 21<br/>using HMAC with SHA-256 and the key<br/>&emsp;0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b<br/>&emsp;0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b.

> 

### Exercise 6.7 - Using an existing cryptography library, compute the MAC of the message<br/>&emsp;4D 41 43 73 20 61 72 65 20 76 65 72 79 20 75 73<br/>&emsp;65 66 75 6C 20 69 6E 20 63 72 79 70 74 6F 67 72<br/>&emsp;61 70 68 79 21<br/>using GMAC with AES and the 256-bit key<br/>&emsp;80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00<br/>&emsp;00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01<br/>and the nonce<br/>&emsp;00 00 00 00 00 00 00 00 00 00 00 01.

> 
