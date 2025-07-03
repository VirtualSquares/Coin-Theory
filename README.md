# Coin-Theory(My first writeup ;D)
# Initial Assumption

- Let the initial state be `x` in `{0 (heads), 1 (tails)}`.
- Each flip adds a number `a_j` in `{1, ..., 8}` chosen uniformly at random.
- The state after `i` flips is:

    S_i = ( x + Σ_{j=1}^i a_j ) mod 2

- The coin face is heads if `S_i = 0`, tails if `S_i = 1`.

---

# Assumption Reasoning

- Since parity determines the face, starting at `x = 0` (heads),  
  the count of heads in `n` flips is:

    Σ_{i=1}^n 1{ S_i = 0 } = Σ_{i=1}^n 1{ ( x + Σ_{j=1}^i a_j ) mod 2 = 0 }

- The assumption was that because the sequence of sums produces more even than odd values,  
  the starting face `x` will always be at least as frequent as the opposite face.

- More formally, it was thought:

    #heads ≥ #tails

or

    #heads = ⎡n/2⎤,   #tails = ⎣n/2⎦   (if x = 0)

---

# Why This is Incorrect

- The increments `a_j` are uniform from 1 to 8, half even and half odd.
- Define parity function `p(a_j) = a_j mod 2`.
- Then:

    S_i = ( x + Σ_{j=1}^i p(a_j) ) mod 2

- Since the values `p(a_j)` are independent and equally likely 0 or 1,  
  the sum Σ p(a_j) mod 2 behaves like a fair coin toss.

- Therefore:

    P(S_i = 0) = P( (Σ p(a_j)) mod 2 = x ) = 0.5

- The expected number of heads in `n` flips is:

    E[#heads] = Σ_{i=1}^n P(S_i = 0) = n/2

- So the starting face does **not** bias the outcome,  
  and over many trials heads and tails occur equally often on average.
