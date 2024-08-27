# Optimization

In mathematics, engineering, computer science, and economics, an **optimization problem** is the problem of finding the _best_ solution from all feasible solutions.

In the more general approach, an **optimization problem**  consists of **maximizing or minimizing** a real function by systematically choosing input values from within an allowed set and computing the value of the function.

Optimization problems can be divided into two categories, depending on whether the variables are **continuous** or **discrete**:

- An optimization problem with discrete variables is known as a *discrete optimization*, in which an object such as an integer, permutation or graph must be found from a countable set.
- A problem with continuous variables is known as a *continuous optimization*, in which an optimal value from a continuous function must be found. They can include constrained problems and multimodal problems.

## Continuous Optimization

- **Variables**: In continuous optimization, the decision variables can take any value within a continuous range or interval. These values can be real numbers (e.g., any number between 0 and 1, or between -∞ and +∞).
    
- **Solution Space**: The solution space is continuous, meaning that there are infinitely many possible solutions. This requires techniques like calculus-based methods (e.g., gradient descent, Newton's method) to find optimal solutions.
    
- **Example Problems**:
    - **Minimizing a function**: Find the minimum value of a smooth function $f(x)$ where $x$ is a real number (e.g., $x \in [0, 10]$).
    - **Linear programming**: Maximizing or minimizing a linear objective function subject to linear equality and inequality constraints, where variables can take any real values within certain bounds.

## Discrete Optimization

- **Variables**: In discrete optimization, the decision variables can only take on specific, distinct values. These values are often integers or belong to a finite set of possibilities.
    
- **Solution Space**: The solution space is discrete, consisting of a finite or countably infinite number of solutions. Since the space is not continuous, methods such as combinatorial algorithms (e.g., dynamic programming, branch and bound, integer programming) are used.
    
- **Example Problems**:
    - **Traveling Salesperson Problem (TSP)**: Finding the shortest possible route that visits a set of cities exactly once and returns to the starting city. The variables represent sequences of cities, which are discrete.
    - **Integer programming**: Similar to linear programming, but the variables are restricted to integer values.


## Local Optimization
Local optimization involves finding a solution that is better than neighboring solutions within a specific region of the solution space. This solution is known as a **local optimum**. For a minimization problem, a local minimum is a point where the objective function is lower than at all nearby points. Similarly, for maximization, a local maximum is higher than at all nearby points.

**Characteristics**:
- A local optimum is the best solution within a neighborhood but may not be the best overall (i.e., it may not be a global optimum).
- Local optima are easier to find than global optima, especially in large or complex problems.
- In convex problems, the local optimum is also the global optimum, but in non-convex problems, local optima can be misleading if the goal is to find the global optimum.


## Global Optimization
Global optimization refers to finding the absolute best solution, or **global optimum**, across the entire feasible solution space. For a minimization problem, this means finding the point where the objective function reaches its lowest possible value globally. For a maximization problem, it’s the point where the objective function is maximized across the entire space.

**Characteristics**:
- The global optimum is the best possible solution overall.
- In non-convex problems, there may be multiple local optima, but only one (or a few, in the case of multiple global optima) global optimum.
- Finding the global optimum can be challenging, especially in complex or high-dimensional spaces where the objective function has multiple peaks and valleys (local optima).

### How is an optimization problem composed?
An optimization problem has three main parts:

1) A finite set $X$ called the *feasible set*, that represents the possibilities we have.
2) A function $f:X \rightarrow \mathbb{R}$ called the *target function* 
3) A $\{max, min\}$ element that indicates if we want to **maximize** or **minimize** our *assessment*.


### How can we represent an optimization problem?
An optimization problem can be represented in the following way:

_Given:_ a function $f:A \rightarrow \mathbb{R}$ from some set $A$ to the real numbers.

_Sought:_ an element $x_0 \in A$ such that $f(x_0) \leq f(x)$ for all $x \in A$ ("minimization") or such that $f(x_0) \geq f(x)$ for all $x \in A$ ("maximization").

Since the following is valid:

$f(x_0) \geq f(x) \leftrightarrow −f(x0) \leq −f(x)$

it suffices to solve only minimization problems. However, the opposite perspective of considering only maximization problems would be valid, too.


## Problem solving
Solve an optimization problem has two possible meanings:

1) Find the *optima* $\alpha^* = min \{f(x):x \in X \}$ where $\alpha \in \mathbb{R}$
2) Find $x$ element with $f(x^*) = \alpha$, $x$ is a problem *optima*. (This is harder than the 1)

##### Observation
An optimization problem could have many optimum values $x^*$, so we define:

$argmin = \{x \in X: f(x) = \alpha \}$ and $argmax$ is defined analogously.


