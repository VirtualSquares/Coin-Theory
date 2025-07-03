# Coin-Theory(My first latex writeup ;D)
# Initial Assumption

- Let the initial state be \( x \in \{0 \text{ (heads)}, 1 \text{ (tails)}\} \).
- Each flip adds a number \( a_j \in \{1, \ldots, 8\} \) chosen uniformly at random.
- The state after \( i \) flips is:
  
  \[
  S_i = \bigg(x + \sum_{j=1}^i a_j\bigg) \bmod 2
  \]

- The coin face is heads if \( S_i = 0 \), tails if \( S_i = 1 \).

---

# Assumption Reasoning

- Since parity determines the face, starting at \( x = 0 \) (heads),  
  the count of heads in \( n \) flips is:

  \[
  \sum_{i=1}^n \mathbf{1}_{\{S_i=0\}} = \sum_{i=1}^n \mathbf{1}_{\{(x + \sum_{j=1}^i a_j) \bmod 2 = 0\}}
  \]

- The assumption was that because the sequence of sums produces more even than odd values,  
  the starting face \( x \) will always be at least as frequent as the opposite face.
- More formally, it was thought:

  \[
  \#\text{heads} \geq \#\text{tails}
  \]

  or

  \[
  \#\text{heads} = \lceil \tfrac{n}{2} \rceil, \quad \#\text{tails} = \lfloor \tfrac{n}{2} \rfloor \quad \text{(if } x = 0 \text{)}
  \]

---

# Why This is Incorrect

- The increments \( a_j \) are uniform from 1 to 8, half even and half odd.
- Define parity function \( p(a_j) = a_j \bmod 2 \).
- Then:

  \[
  S_i = \left(x + \sum_{j=1}^i p(a_j)\right) \bmod 2
  \]

- Since \( p(a_j) \) are independent and equally likely 0 or 1,  
  the sum \( \sum p(a_j) \bmod 2 \) behaves like a fair coin toss.
- Therefore:

  \[
  P(S_i = 0) = P\left(\sum p(a_j) \bmod 2 = x \right) = \frac{1}{2}
  \]

- The expected number of heads in \( n \) flips is:

  \[
  \mathbb{E}[\#\text{heads}] = \sum_{i=1}^n P(S_i=0) = \frac{n}{2}
  \]

- So the starting face does **not** bias the outcome,  
  and over many trials heads and tails occur equally often on average.
