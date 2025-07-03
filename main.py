"""
Initial assumption:

- Let the initial state be x ∈ {0 (heads), 1 (tails)}.
- Each flip adds a number a_j ∈ {1,...,8} chosen uniformly at random.
- The state after i flips is:
    S_i = (x + ∑_{j=1}^i a_j) mod 2

- The coin face is heads if S_i = 0, tails if S_i = 1.

Assumption reasoning:

- Since parity determines the face, starting at x = 0 (heads),
  the count of heads in n flips is:
    ∑_{i=1}^n 1_{S_i=0} = ∑_{i=1}^n 1_{(x + ∑_{j=1}^i a_j) mod 2 = 0}
- The assumption is that because the sequence of sums produces more even than odd values,
  the starting face x will always be at least as frequent as the opposite face.
- More formally, it was thought:
    #heads ≥ #tails
  or
    #heads = ⎡n/2⎤, #tails = ⎣n/2⎦  (if x = 0)

Why this is incorrect:

- The increments a_j are uniform from 1 to 8,
  half of which are even and half are odd.
- Define parity function p(a_j) = a_j mod 2.
- Then:
    S_i = (x + ∑_{j=1}^i p(a_j)) mod 2
- Since p(a_j) are independent and equally likely 0 or 1,
  ∑ p(a_j) mod 2 behaves like a fair coin toss.
- Therefore:
    P(S_i = 0) = P(∑ p(a_j) mod 2 = x) = 0.5
- The expected number of heads in n flips:
    E[#heads] = ∑_{i=1}^n P(S_i=0) = n/2
- So the starting face does not bias the outcome,
  and over many trials heads and tails occur equally often on average.
"""

import random

def simulateCoinFlips(trials, coins):
    totalHeadsPercentage = 0
    totalTailsPercentage = 0

    for _ in range(trials):
        heads = 0
        for _ in range(coins):
            flip = (1 + random.randint(1, 8)) % 2
            if flip == 1:
                heads += 1
        tails = coins - heads
        totalHeadsPercentage += heads / coins * 100
        totalTailsPercentage += tails / coins * 100

    avgHeads = totalHeadsPercentage / trials
    avgTails = totalTailsPercentage / trials

    return avgHeads, avgTails

avgHeads, avgTails = simulateCoinFlips(100000, 10)
print(f"Average heads percentage: {avgHeads:.2f}%")
print(f"Average tails percentage: {avgTails:.2f}%")
