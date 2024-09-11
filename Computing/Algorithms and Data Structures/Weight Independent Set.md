# Weight Independent Set


## Independent Set
An **independent set**, **stable set**, **coclique** or **anticlique** is a set of vertices in a graph, no two of which are adjacent. That is, it is a set $S$ of vertices such that for every two vertices in $S$, there is no edge connecting the two.

A set is independent if and only if it is a clique in the graph's complement.

Two sets $A$ and $B$ are said to be independent if their intersection $A \cap B = \emptyset$, where $\emptyset$ is the empty set. For example, $\{A,B,C\}$ and $\{D,E\}$ are independent, but $\{A,B,C\}$ and $\{C,D,E\}$ are not. Independent sets are also called disjoint or mutually exclusive.

![IndependentSet](IndependentSet.png)

## Maximum Weight Independent Set

The **Maximum Weight Independent Set Problem (WIS)** is a well-known NP-hard problem. A popular way to study WIS is to detect graph classes for which WIS can be solved in polynomial time, with particular reference to hereditary graph classes, i.e., defined by a hereditary graph property or equivalently by forbidding one or more induced subgraphs.

Is a variation of the independent set problem in graph theory, but it takes vertex weights into account.

The **Maximum Weight Independent Set (WIS)** seeks to find an independent set in a weighted graph where the sum of the weights of the vertices in the set is maximized. Unlike the standard independent set problem (which may just seek the largest set by the number of vertices), WIS focuses on the **total weight** of the set rather than the number of vertices.

**Complexity**: The WIS problem is generally **NP-hard**, meaning it is computationally difficult to solve exactly for large graphs.

**Applications**: It can be used in various scenarios like scheduling (where tasks cannot overlap), resource allocation, wireless networks (where interference must be minimized), and more.

