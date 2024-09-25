# Knapsack

The **knapsack problem** is the following problem in combinatorial optimization:

*"Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible".*

It derives its name from the problem faced by someone who is constrained by a fixed-size **knapsack** and must fill it with the most valuable items. The problem often arises in resource allocation where the decision-makers have to choose from a set of non-divisible projects or tasks under a fixed budget or time constraint, respectively.

The most common problem being solved is the **0-1 knapsack problem**, which restricts the number $x_i$ of copies of each kind of item to $0$ or $1$. Given a set of $n$ items numbered from $1$ up to $n$, each with a weight $w_i$ and a value $v_i$, along with a maximum weight capacity $W$,

$$maximize \sum_{i=1}^{n} v_i x_i$$

$$\textrm{subject to} \sum_{i=1}^{n} w_i x_i \le W \quad \textrm{and}\quad x_i \in \{0,1,2,...,c\}$$
Here $x_i$ represents the number of instances of item $i$ to include in the knapsack. Informally, the problem is to maximize the sum of the values of the items in the knapsack so that the sum of the weights is less than or equal to the knapsack's capacity.

## **Algorithm** (0/1 Knapsack)
The input to the problem is the following: the weight of   $i^{th}$  item   $w_i$ , the value of $i^{th}$ item $v_i$ , and the total capacity of the knapsack   $W$.
Let  $dp_{i, j}$  be the [[Dynamic Programming|dynamic programming]] state holding the maximum total value the knapsack can carry with capacity $j$, when only the first $i$  items are considered.

Assuming that all states of the first  $i-1$ items have been processed, what are the options for the   $i^{th}$  item?

- When it is not put into the knapsack, the remaining capacity remains unchanged and total value does not change. Therefore, the maximum value in this case is $dp_{i-1,j}$
- When it is put into the knapsack, the remaining capacity decreases by   $w_i$  and the total value increases by  $v_i$, so the maximum value in this case is   $dp_{i-1,j-w_i}+v_i$

From this we can derive the *dp* transition equation:
$$dp_{i,j}=max\{dp_{i-1,j}, \;dp_{i-1, j-w_i}+v_i\}$$

Or what is the same:

$$K(n, W) = max\{K(n-1, W), v_n + K(n-1, W-w_n)\}$$


### Code Implementation using Dynamic Programming (Rust)

```
pub fn knapsack(capacity: usize, items: Vec<KnapsackItem>) {  
    let n = items.len();  
    let mut dp = DMatrix::repeat(n + 1, capacity + 1, 0);  
  
    for i in 1..=n {  
        for w in 0..=capacity {  
            if i == 0 || w == 0 {  
                dp[(i, w)] = 0;  
            } else if items.get(i - 1).unwrap().weight <= w {  
                dp[(i, w)] = max(items.get(i - 1).unwrap().value + dp[(i - 1, w - items.get(i - 1).unwrap().weight)], dp[(i - 1, w)]);  
            } else {  
                dp[(i, w)] = dp[(i - 1, w)];  
            }  
        }  
    }  
}
```

### **Knapsack for 2 bags**

This problem is a variant of the classical **Knapsack problem**, but with two knapsacks (or bags) with integer capacities $W_1$​ and $W_2$​, and a collection of $n$ items. The goal is to divide the items into two disjoint subsets $K_1$​ and $K_2$​, so that we maximize the total value of the items in both knapsacks, while respecting the capacity constraints.

### Definitions

- $W_1$ and $W_2$​: the **capacities** of knapsacks 1 and 2, respectively.
- $v_i$: the **value** of item $i$.
- $w_i$: the **weight** of item $i$.
- $K_1$ and $K_2$​​: the sets of items placed in knapsacks 1 and 2, respectively.
- $V(K_1,K_2)$ = $\sum_{i\in K_1}v_i\;+\;\sum_{i \in K_2}v_i$: the total value of items in both knapsacks.
- Constraints: 
	- $\sum_{i\in K_1}w_i \le W_1$ 
	- $\sum_{i\in K_2}w_i \le W_2$
	- $K_1 \bigcap K_2 \;=\; \emptyset$

We define a state $dp(i,c_1,c_2)$, which represents the maximum value we can obtain considering the first $i$ items and the remaining capacities $c_1$ and $c_2$ in knapsacks 1 and 2, respectively.

**Recurrence Relation (Bellman Equation):**
For each item $i$, we have three choices:

1. Do not include $i$ in either knapsacks
2. Include $i$ in knapsack 1 (if it fits).
3. Include $i$ in knapsack 2 (if it fits).

The recurrence relation is: 
$$
 \begin{align}
    dp(i,c_1,c_2) = \begin{dcases*}
        max(dp(i-1,c_1,c_2),\;dp(i-1,c_1-w_i,c_2)+i_v),& if $ c_1 \ge w_i $,\\
        max(dp(i-1,c_1,c_2),\;dp(i-1,c_1,c_2-w_i)+i_v), & if $ c_2 \ge w_i $
        \end{dcases*}
  \end{align}
$$

Where: 
- $dp(i-1,c_1,c_2)$ represents the option of not taking item $i$.
- $dp(i-1,c_1-w_i,c_2)+i_v)$ represents the option of placing $i$ in knapsack 1, as long as the remaining capacity $c_1$ is sufficient.
- $dp(i-1,c_1,c_2-w_i)+i_v)$ represents the option of placing $i$ in knapsack 2, as long as the remaining capacity $c_2$ is sufficient.


$dp(0,c_1,c_2) = 0$, since if there are no items, the total value is 0.


chequear el practico 2