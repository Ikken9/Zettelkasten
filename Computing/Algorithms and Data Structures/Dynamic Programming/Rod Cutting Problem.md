# Rod Cutting Problem

Given a rod of length n and an array of prices that includes prices of all pieces. We have predefined (positive integers) lengths $l_1 \lt \cdots \lt l_k$ and fixed prices (positive reals) $p_1, \cdots, p_k$ for each length.

We want to cut a **rod** of length $L$ in $x_i$ pieces of $l_i$ lengths so that the profit is maximized.


Let $dp(L)$ be the maximum profit for cutting a rod of length $L$. The state space consists of all possible lengths from 0 to $L$, where each state $dp(L)$ represents the best profit that can be obtained from a rod of length $L$.

#### Bellman Equation:
The Bellman equation for the rod cutting problem can be defined as follows:


$$dp(L) = \max_{1 \leq i \leq k} (p_i + dp(L - l_i) \mid l_i \le L)$$


Where:
- $p_i$ is the price of the $i$-th piece with length $l_i$
- $dp(L - l_i)$ is the maximum profit for the remaining length $L - l_i$

If the length of the rod is less than the current piece $l_i$, then that piece cannot be used.

### Algorithm:

1. **Initialize the DP table**: 
   
   $dp[0] = 0$
   
   Set the base case where the maximum profit for a rod of length 0 is 0 (no rod, no profit).

2. **Fill the DP table**:
   For each length $l = 1$ to $L$, iterate over each possible piece $i = 1$ to $i = k$, and compute the maximum profit for that length by comparing the current value in the $DP$ table and the potential profit from using a piece of length $l_i$:
   
   
   $$dp[L] = \max(dp[L], p_i + dp[L - l_i]) \quad \text{for all } l_i \leq L$$
   

3. **Return the result**: 
   The maximum profit for a rod of length $L$ will be stored in $dp[L]$.

**Transition between states**: Each state $dp(L)$ is built upon the maximum profit for shorter rod lengths, considering all valid ways to cut the rod using available lengths $l_1, l_2, \dots, l_k$.
