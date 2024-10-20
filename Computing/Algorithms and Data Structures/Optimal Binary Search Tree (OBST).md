# Optimal Binary Search Tree (OBST)

An **Optimal Binary Search Tree (OBST)**, also known as a **Weighted Binary Search Tree**, is a [[Binary Search Tree (BST)|binary search tree]] that minimizes the expected search cost. In a binary search tree, the search cost is the number of comparisons required to search for a given key.

In an **OBST**, each node is assigned a weight that represents the probability of the key being searched for. The sum of all the weights in the tree is $1.0$. The expected search cost of a node is the sum of the product of its depth and weight, and the expected search cost of its children.

The search time can be improved, placing the most frequently used data in the root and closer to the root element, while placing the least frequently used data near leaves and in leaves.

There can be more than one optimal tree. The number of binary trees on $n$ nodes turns out to be $$\frac{\binom{2n}{n}}{n+1}$$
## **Finding the optimal tree (successful search only)**

***How can we find an optimal tree, given the access frequency of each key?***

A brute-force approach that checks each of the possible binary search trees is impractical, because there are far too many trees to check.

Let the keys be {$K_1 \lt K_2 \lt \cdots \lt K_n$} in their dictionary order (sorted by their probability), and let $p(i)$ be the probability of accessing $k_i$. Thus: $$\sum_{i=1}^n p(i) = 1$$
Now let $1 \le j \le k \le n$, and let $T$ be any tree constructed from the keys $K_j, \cdots, K_k$.

We define $Depth_T(K_i)$, where $j \le i \le k$, to be the depth in $T$ of the node where $K_i$ is stored, and define the cost of $T$ to be $C(T) = \sum_{i=j}^k p(i)(Depth_T(K_i) + 1)$

If $j = 1$ and $k = n$ then the cost is the expected number of comparisons to find a key in the tree, **that equals to the level of the key in $T$**; if $T$ holds only a subset of the keys then $C(T)$ represents the cost of searching within the tree for only those keys, with searches for other keys regarded as free. We extend our previous terminology by saying that any tree $T$ is optimal if its cost is as small as the cost of any other tree with the same keys.

Our objective is to find a tree $T$ on all $n$ keys that minimizes $C(T)$. The crucial observation in reducing the number of trees to be considered is that ***every subtree of an optimal tree is itself optimal***. We want a balanced tree where the $K$ keys whose frequency is higher are located in an orderly manner, where the key with the highest frequency is the root.

That is, if $T$ is an optimal tree for $K_j, \cdots, K_k$ and its root is $K_r$, then its left subtree must be an optimal tree for $K_j, . . . , K_{r-1}$, and its right subtree must be an optimal tree for $K_{r+1}, \cdots, K_k$.

```tikz
\usepackage{tikz}

\begin{document}

\begin{tikzpicture}
    % Root node
    \node[circle, draw, fill=white] (root) at (0,0) {Root};

    % Left subtree (triangle representation) - moderately larger triangle
    \filldraw[fill=white!20, draw=black] 
        (-3.5,-2) -- (-1,-5) -- (-6,-5) -- cycle;
    \node at (-3.5,-4) {\Large $K_j, \cdots, K_{r-1}$}; % Larger text and adjusted position

	% Caption for the left triangle 
	\node at (-3.5,-5.5) {\Large $T_L$};

    % Right subtree (triangle representation) - moderately larger triangle
    \filldraw[fill=white!20, draw=black] 
        (3.5,-2) -- (6,-5) -- (1,-5) -- cycle;
    \node at (3.5,-4) {\Large $K_{r+1}, \cdots, K_k$}; % Larger text and adjusted position

	% Caption for the right triangle 
	\node at (3.5,-5.5) {\Large $T_R$};

    % Edges from root to subtrees
    \draw (root) -- (-3.5,-2); 
    \draw (root) -- (3.5,-2);

\end{tikzpicture}

\end{document}
```


If the left and right subtrees of $T$ are $T_L$ and $T_R$ (both optimal trees), then the depth of each node of $T_L$ or $T_R$ increases by one when it is viewed as a node of $T$.

So it follows that if $K_l$ is at the root of $T$ then:

$$
\begin{equation}
\begin{aligned}
C(T) &= p_r + \sum_{i=j}^{r-1} p_i(Depth_T(K_i)+1) + \sum_{i=r+1}^{k}p_i(Depth_T(K_i)+1) \\
& = p_r + \sum_{i=j}^{r-1}p_i + C(T_L) + \sum_{i=r+1}^{k} p_i + C(T_R)\\
& = \sum_{i=j}^k p_i + C(T_L) + C(T_R)
\end{aligned}
\end{equation}
$$

Therefore replacing $T_L$ or $T_R$ by any tree on the same nodes with lower cost would result in a tree of lower cost than $T$.


## **Construction**

#### Note: 
In many cases, the **dummy keys** (and their corresponding frequencies) are not considered when constructing an **Optimal Binary Search Tree (OBST)** because the focus is solely on **successful searches**, meaning the probability of searching for an element in the tree is given only for the actual keys.

In some applications, **unsuccessful searches** may not be important or relevant. The application could guarantee that every search will always find a matching key (perhaps through pre-processing or ensuring that only valid keys are searched).

To construct the **Optimal BST** we need to find the Bellman equation that captures the optimal substructure of the problem and forms the basis for the dynamic programming solution.

The **Bellman equation** for the optimal binary search tree is a recursive formulation that defines the optimal solution in terms of smaller subproblems. Let $\Lambda(i, j)$ denote the **minimum** expected search cost for the subtree containing the keys $k_i,k_{i+1}, \cdots, k_j​$. The Bellman equation is:

$$\Lambda(i, j) = \min_{r=i}^{j} \{ \Lambda(i, r-1) + \Lambda(r+1, j) + W(i, j) \}$$
Where:

- $W(i,j) = \sum_{k=i}^{j}p_k$​ is the total probability of searching any key between $k_i$​ and $k_j$.
- $\Lambda(i, r-1)$ is the optimal search cost for the left subtree.
- $\Lambda(r+1, j)$ is the optimal search cost for the right subtree.
- $r$ is the root of the current subtree.

### *The process is the following:*

Create an $n \times n$ matrix where $n$ is the number of keys where $\text{cost}[i][j]$ represents the optimal cost of a BST containing keys from index $i$ to $j$

**Base Cases**:
- For single keys (when $i = j$), the cost is simply the frequency of that key
- These form the diagonal of our matrix (if we start the matrix from $n$, if instead we start from 0, then the diagonal is will be filled with 0s)

We fill the matrix diagonally, considering chains of increasing length.

**Final Result**: The optimal cost is stored in $\text{cost}[0][n-1]$ and it represents the optimal cost of the OBST.



> [!exercise]
> Given the $n$ keys $(K_1  = 10), (K_2 = 20), (K_3 = 30), (K_4 = 40)$ and their corresponding frequencies $4, 2, 6, 3$, find the OBST.
> 
> We construct an empty ($\text{0 to n+1}) \times (\text{0 to n+1})$ matrix starting from $0$. (This step can be omitted and start directly from $n$):
> $$
> \begin{array}{|c|c|c|c|c|} 
> \hline   & 0 & 1 & 2  & 3 & 4 \\ 
> \hline 0 &  &  &  &  \\ 
> \hline 1 &  &  &  &  \\ 
> \hline 2 &  &  &  & \\
> \hline 3 &  &  &  & \\
> \hline 4 &  &  &  & \\
> \hline \end{array}
> $$
>First, we will calculate the values where $j-i$ is equal to $0$.
>When $i=0$, $j=0$, then $j-i = 0$
>When $i = 1$, $j=1$, then $j-i = 0$
>When $i = 2$, $j=2$, then $j-i = 0$
>When $i = 3$, $j=3$, then $j-i = 0$
>When $i = 4$, $j=4$, then $j-i = 0$
>
>Therefore, $c[0, 0] = 0$, $c[1 , 1] = 0$, $c[2,2] = 0$, $c[3,3] = 0$, $c[4,4] = 0$, where $c$ is the **cost**.
>
>Now we populate the matrix with that values in $[0, 0]$, $[1, 1]$, $[2, 2]$, $[3, 3]$, $[4, 4]$:
>This step is just filling the matrix diagonal with zeroes.
> $$
> \begin{array}{|c|c|c|c|c|} 
> \hline   & 0 & 1 & 2 & 3 & 4\\ 
> \hline 0 & 0 &   &   &   &  \\ 
> \hline 1 &   & 0 &   &   &  \\ 
> \hline 2 &   &   & 0 &   &  \\
> \hline 3 &   &   &   & 0 &  \\
> \hline 4 &   &   &   &   & 0\\
> \hline \end{array}
> $$
> 
>Now we need to consider all the trees that can be made with one node, so we to find the values where $j-i$ equal to $1$:
>When $j=1$, $i=0$, then $j-i = 1$
>When $j=2$, $i=1$, then $j-i = 1$
>When $j=3$, $i=2$, then $j-i = 1$
>When $j=4$, $i=3$, then $j-i = 1$
>
>So to calculate the cost, we will consider only the $j^\text{th}$ value of $c[i,j]$.
> 
>The cost of $c[0,1]$ is $4$ (The key $j_1$ is $10$, and the corresponding cost is $4$).
>The cost of $c[1,2]$ is $2$ (The key $j_2$ is $20$, and the corresponding cost is $2$).
>The cost of $c[2,3]$ is $6$ (The key $j_3$ is $30$, and the corresponding cost is $6$).
>The cost of $c[3,4]$ is $3$ (The key $j_4$ is $40$, and the corresponding cost is $3$).
> 
> $$
> \begin{array}{|c|c|c|c|c|} 
> \hline   & 0 & 1 & 2 & 3 & 4\\ 
> \hline 0 & 0 & 4 &   &   &  \\ 
> \hline 1 &   & 0 & 2 &   &  \\ 
> \hline 2 &   &   & 0 & 6 &  \\
> \hline 3 &   &   &   & 0 & 3\\
> \hline 4 &   &   &   &   & 0\\
> \hline \end{array}
> $$
> 
>Now we need to consider all the trees that can be made with two nodes (a chain of two), so we need to find the values where $j-i$ equal to $2$:
>When $j=2$, $i=0$, then $j-i = 2$
>When $j=3$, $i=1$, then $j-i = 2$
>When $j=4$, $i=2$, then $j-i = 2$
>
>So first we calculate the sum of the frequencies of the nodes that we're considering, first $K_1$ and $K_2$, so it would be:
>
>$\sum_{K_1}^{K_2}p_K = 4 + 2 = 6$
>
>and now we need to find all the possible options to create a BST using two nodes and calculate the cost for each:
>
>First option: $K_1$ as root: $\sum_{K_1}^{K_2}p_K = 6 + p_{K_1} = 4 = 10$
>Second option: $K_2$ as root: $\sum_{K_1}^{K_2}p_K = 6 + p_{K_2} = 2 = 8$
>
>We take the minimum and add it to the matrix.
> $$
> \begin{array}{|c|c|c|c|c|} 
> \hline   & 0 & 1 & 2 & 3 & 4\\ 
> \hline 0 & 0 & 4 & 8 &   &  \\ 
> \hline 1 &   & 0 & 2 &   &  \\ 
> \hline 2 &   &   & 0 & 6 &  \\
> \hline 3 &   &   &   & 0 & 3\\
> \hline 4 &   &   &   &   & 0\\
> \hline \end{array}
> $$
> 
>Now we consider $K_2$ and $K_3$ 
 



#### Time and Space Complexity
Time complexity is $O(n^3)$ because there are $n^2$ states and each minimum has $n$ terms.