# Weight Independent Set


## Independent Set
An **independent set**, **stable set**, **coclique** or **anticlique** is a set of vertices in a graph, no two of which are adjacent. That is, it is a set $S$ of vertices such that for every two vertices in $S$, there is no edge connecting the two.

A set is independent if and only if it is a clique in the graph's complement.

Two sets $A$ and $B$ are said to be independent if their intersection $A \cap B = \emptyset$, where $\emptyset$ is the empty set. For example, $\{A,B,C\}$ and $\{D,E\}$ are independent, but $\{A,B,C\}$ and $\{C,D,E\}$ are not. Independent sets are also called disjoint or mutually exclusive.

![IndependentSet](IndependentSet.png)


## **Maximum Weight Independent Set**
The **Maximum Weight Independent Set Problem (WIS)** is a well-known NP-hard problem. A popular way to study **WIS** is to detect graph classes for which **WIS** can be solved in polynomial time, with particular reference to hereditary graph classes, i.e., defined by a hereditary graph property or equivalently by forbidding one or more induced subgraphs.

Is a variation of the independent set problem in graph theory, but it takes vertex weights into account.

**WIS** seeks to find an independent set in a weighted graph where the sum of the weights of the vertices in the set is maximized. Unlike the standard independent set problem (which may just seek the largest set by the number of vertices), WIS focuses on the **total weight** of the set rather than the number of vertices.

**Applications**: It can be used in various scenarios like scheduling (where tasks cannot overlap), resource allocation, wireless networks (where interference must be minimized), and more.



## **Optimal Solution**
Given a graph $G$ and a subset $W$ of all vertices of $G$, symbolically: $W \subseteq V(G)$, we define $S$ as the graph that contains all the vertices of $G$ that are in $W$, essentially all the vertices that are in $W$ (because of $W \subseteq V(G)$), and whose edges are the edges of $G$ that have both ends on $V (G) \backslash W$.

Note: $W$ is a subset, not a graph, $S$ is the graph containing the vertices of $W$.

If $G$ is a non-directed finite graph with $v_1, ...,  v_n$ as vertices, endowed with a function of positive weights on the vertices called $w$ then, the following is defined:

$$WIS(G) = max \{w(S) : S \subseteq V (G)\; and \;S \;is \;independent \;on \;G\}$$
where:

$w(S) = \sum_{s\in S}(s)$

That means, $WIS$ is a function that maximizes the weights of the vertices of an independent set $W$ that contains the vertices of $G$.


Let's suppose that $S^*$ is the optimal solution, that is: $w(S*)=WIS(G_n)$, then we ask ourselves if the last vertex $V_n$ is included or not in $S^*$:

- If it's **NOT INCLUDED** then, all vertices of $S^*$ belong to  $G_{n-1}$, so the solution will be: $$w(S^*)=WIS(G_{n-1})$$
- If it's **INCLUDED** then, the vertex $v_{n-1}$ is not included since $S^*$ is an [[Weight Independent Set#Independent Set|independent set]], so the solution will be: $$w(S^*)=w(n)+WIS(G_{n-2})$$
As we need to consider both options, the solution is the one that has the maximum weighted independent set (as the problem states), that is: $$max\{WIS(G_{n-1}), \;w(n)+WIS(G_{n-2})\}$$

### WIS on string graphs

For any string graph with positive weights, the next algorithm produces an maximum weight independent set:

1) We use the Bellman Equation to calculate the vector: $$A[i]=WIS(G_i)$$
2) We iterate over the vector $A$ backwards selecting the vertices of the *MWIS*

It has a time complexity of $O(n)$


**Example**:

```tikz
\usepackage{tikz} 
\begin{document} 
\begin{tikzpicture}[scale=1, every node/.style={circle, draw, minimum size=0.8cm, inner sep=0pt}]
\node (v3) at (0,0) {3}; 
\node (v2) at (2,0) {2}; 
\node (v1) at (4,0) {1}; 
\node (v6) at (6,0) {6}; 
\node (v4) at (8,0) {4}; 
\node (v5) at (10,0) {5}; 

\draw (v3) -- (v2); 
\draw (v2) -- (v1); 
\draw (v1) -- (v6); 
\draw (v6) -- (v4); 
\draw (v4) -- (v5); 
\end{tikzpicture} 
\end{document}
```


$WIS(G_1)=3$

$WIS(G_2)=3$, as the maximum weighted independent set we can create considering $G_1$ and $G_2$ is still $3$

$WIS(G_3)=max\{w(s) + WIS(G_{n-2}), WIS(G_{n-1})\} = max\{w(v_3)+3, 3\}=4$

$WIS(G_4) = max\{6 + WIS(G_2), WIS(G_3)\} = max\{6 + 3, 4\} = 9$

$WIS(G_5) = max\{4 + WIS(G_3), WIS(G_4)\} = max\{4 + 4, 9\} = 9$

$WIS(G_6)=max\{5 + WIS(G_4), WIS(G_5)\} = max\{5 + 9, 9\}=14$


**But how can we know which vertices to add to the solution?**
Well, starting from the end, we need to look at the $max$ function on each step, and check which value is greater. If the greater value is "$w(s) + WIS(G_{n-2})$", then we add the vertex to the solution, otherwise not.

