# Chapter 16 - The Clock

## Exercises

### Exercise 16.1

Some computers use NTP at boot, or at regular intervals. Turn off NTP for one week on your computer. Write a program that at regular intervals (at least once every two hours) records both the true time and the time reported by your computer. Let t0 be the initial true time at the start of your experiment. For each time measurement pair, plot the true time minus $t_{0]$ on the horizontal axis of a graph and plot your computer’s time minus true time on the vertical axis. How different is your computer’s clock from true time after one week? Does your graph tell you anything else?

#### Solution

Not exactly going to do this, but we can instead compare times of two NTP servers, and for that, check out this [Gist](https://gist.github.com/crashdump/5704286).

### Exercise 16.2

Repeat exercise 16.1, but this time for a collection of five different computers.

#### Solution

Skip.

### Exercise 16.3

Find a new product or system that uses (or should use) a clock. This might be the same product or system you analyzed for Exercise 1.8. Conduct a security review of that product or system as described in Section 1.12, this time focusing on the security and privacy issues surrounding the clock.

#### Solution

Skip.
