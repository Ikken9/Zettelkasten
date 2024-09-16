# Dynamic Programming

Dynamic programming is both a mathematical optimization method and an algorithmic paradigm, where an algorithmic problem is first broken down into sub-problems, the results are saved, and then the sub-problems are optimized to find the overall solution (which usually has to do with finding the maximum and minimum range of the algorithmic query.

This is done by defining a sequence of **value functions** $V_1, V_2, V_3, \ldots, V_n$ taking _y_ as an argument representing the **state** of the system at times $i$ from $1$ to $n$.

## Bellman Equation
The **Bellman Equation** is a key principle in **dynamic programming**, used to break down a decision problem into simpler, recursive subproblems. It expresses the relationship between the value of a decision at a certain point and the value of subsequent decisions. The equation is typically used in **optimization problems** like shortest paths, resource allocation, and reinforcement learning (Markov Decision Processes).

In dynamic programming, the Bellman Equation helps in finding the **optimal policy** by solving the problem **backwards**, starting from the final state and recursively determining the best course of action.

