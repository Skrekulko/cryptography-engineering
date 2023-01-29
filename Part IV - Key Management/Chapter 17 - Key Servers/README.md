# Chapter 17 - Key Servers

## Exercises

### Exercise 17.1

For the protocol in Section 17.3, what is a reasonable lifetime to use for the keys $K^{'}_{A}$? Why? What bad things could happen if the lifetime is longer? What bad things could happen if the lifetime is shorter?

#### Solution

A key lifetime of a few hours seems reasonable for most situations. In case of the key lifetime being longer, a compromised key would allow the attacker to get access to things for a longer period of time. In case of the key lifetime being shorter, it would most likely unnecessary load for the key server.

### Exercise 17.2

For the protocol in Section 17.3, how might an attacker be able to learn $K^{'}_{A}$ *before* it times out? What bad things would the attacker be able to do with that knowledge? What bad things would the attacker not be able to do with that knowledge?

#### Solution

The attacker might be able to learn the key $K^{'}_{A}$ by acting as the key server. If the attacker learns the key *before* it times out, any communication done with that key is exposed to the attacker. The attacker would only be able to compromise the security of the current communication, until the key expires, but this doesn't apply to older or future communications done with a new key.

### Exercise 17.3

For the protocol in Section 17.3, how might an attacker be able to learn $K^{'}_{A}$ *after* it times out? What bad things would the attacker be able to do with that knowledge? What bad things would the attacker not be able to do with that knowledge?

#### Solution

The attacker might be able to learn the key $K^{'}_{A}$ by acting as the key server. If the attacker learns the key *after* it times out, any communication done with that key up until that point is exposed to the attacker, but not any future ones, since the expired key is not being used anymore.

### Exercise 17.4

For the protocol in Section 17.3, consider an attacker who intercepts all communications. Can the attacker retroactively read data between Alice and Bob if $K_{A}$ and $K_{A}$ are both later exposed?

#### Solution

If the attacker manages to somehow get the $K_{A}$ and $K_{B}$ key, he might be able to then get access to the $K^{'}_{A}$ and $K^{'}_{B}$, and thus also the  $K_{AB}$ key for communication between Alice and Bob.

### Exercise 17.5

For the protocol in Section 17.3, could an attacker gain any advantage in breaking the protocol by forcibly rebooting the key server?

#### Solution

Since the key server doesn't keep track of which keys between users have been set up, the reboot should not compromise the system, even tho the users would have to wait to the key server to come back online.

### Exercise 17.6

For the protocol in Section 17.3, could an attacker mount a denial-of-service attack against two parties wishing to communicate, and if so, how?

#### Solution

Keep rebooting the server, as done in the previous exercise.

### Solution 17.7

For the protocol in Section 17.3, are there policy or legal risks with having the key server generate $K_{AB}$? Are there things Alice and Bob would not say in a situation where the key server generates $K_{AB}$ that they would say if the key were known only to them?

#### Solution

I'm not sure I understand this exercise... Check the chapter if needed, otherwise skip.
