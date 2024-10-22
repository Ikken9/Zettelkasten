# Bellman-Ford Algorithm

The **Bellman–Ford algorithm** is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a **weighted *digraph*** (directed graph). It is slower than [[Dijkstra's Algorithm|Dijkstra's algorithm]] for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

Negative weight edges are used to explain a lot of phenomena like cashflow, the heat released/absorbed in a chemical reaction, etc.
For instance, if there are different ways to reach from one chemical A to another chemical B, each method will have sub-reactions involving both heat dissipation and absorption.

If we want to find the set of reactions where minimum energy is required, then we will need to be able to factor in the heat absorption as negative weights and heat dissipation as positive weights.


## **The idea behind the algorithm**
The Bellman-Ford algorithm’s primary principle is that it starts with a single source and calculates the distance to each node. The distance is initially unknown and assumed to be infinite, but as time goes on, the algorithm relaxes those paths by identifying a few shorter paths. Hence it is said that Bellman-Ford is based on [[Edge Relaxation|Edge Relaxation]].

It states that for the graph having $n$ vertices, all the edges should be relaxed $n-1$ times to compute the single source shortest path.

Given a finite graph $G$ endowed with a function $l$ that assigns random weights to each edge, $l: E(G) \rightarrow \mathbb{R}$, where $E(G)$ is the set of edges of $G$ and let $s \in V(G)$, where $s$ is the start vertex on the set of vertex $V(G)$:

$$\varphi(k, v) = \min\{l(P)\}$$

Where: 
- $v \in V(G)$
- $k \in \mathbb{N}$
- $P$ is a path from $s$ to $v$ using up to $k$ edges of $G$ ($p$ uses $\le k$ edges)

The condition $\le$ naturally arises because the maximum number of edges in any path between two vertices in a graph is limited by the structure of the graph itself. Specifically: $$k \leq |V(G)| - 1$$That is the upper bound in a connected graph ***without cycles***, where $|V(G)|$ is the number of vertices. Any simple path (without revisiting nodes) between two vertices can use at most $|V(G)| - 1$ edges. It serves as a flexible way to represent how far we are allowed to explore paths in the graph in terms of edge count.

### **Negative cycles**
A **negative weight cycle** (or negative loop) occurs when there is a cycle in the graph such that the sum of the weights of the edges in the cycle is negative. This leads to a special scenario: every time we traverse the cycle, the total path weight decreases further.

In the presence of a negative weight cycle, the value of $\varphi(k, v)$ can keep decreasing as more edges are added to the path (i.e., as $k$ increases).

As $k \to \infty$ (i.e., more edges can be used), $\varphi(k, v)$ approaches to $-\infty$ because there is no bound to how negative the weight can become when traversing the negative cycle repeatedly.




## **Algorithm**
Let us assume that the graph contains no negative weight cycle. The case of presence of a negative weight cycle will be discussed below in a separate section.

We will create an array of distances $d[0 \ldots n-1]$, which after execution of the algorithm will contain the answer to the problem. In the beginning we fill it as follows: $d[v] = 0$ , and all other elements $d[ ]$ equal to infinity $\infty$ .

The algorithm consists of several phases. Each phase scans through all edges of the graph, and the algorithm tries to produce **relaxation** along each edge $(a,b)$ having weight   $c$ . Relaxation along the edges is an attempt to improve the value $d[b]$ using value  $d[a] + c$ . In fact, it means that we are trying to improve the answer for this vertex using edge   $(a,b)$ and current answer for vertex  $a$ .

It is claimed that $n-1$ phases of the algorithm are sufficient to correctly calculate the lengths of all shortest paths in the graph (again, we believe that the cycles of negative weight do not exist). For unreachable vertices the distance $d[ ]$ will remain equal to infinity  $\infty$ .

> [!lemma|*]
> 1) If $\varphi(k, v) = \varphi(k+1, v) \; \forall v \in V(G)$  then, $\varphi(k, v) = \min\{l(P)\}$
>    That is, if the values of $\varphi(k, v)$ do not change when we increase the number of edges from $k$ to $k+1$, for every vertex $v \in V(G)$, then we have already found the minimum weight of any path from $s$ to $v$ using at most $k$ edges.
> 2) If $G$ does not have negative cycles ($l(P) < 0$) then, $\varphi(k-1, v) = \varphi(k, v) \; \forall v \in V(G)$
>    That is, if the graph $G$ does not contain negative weight cycles, then the shortest paths from $s$ to any vertex $v$ will stabilize after $n−1$ iterations, i.e., after considering paths with up to $n−1$ edges.

### **Bellman Equation**

So we need to calculate $\varphi(n-1,v)$ and $\varphi(n,v)$ $\forall v \in V$ and there are two possibilities, the first is when the shortest paths have been found, and there are no negative weight cycles, and the second is that a negative weight cycle exists in the graph:

1) $\forall v \; [\varphi(n-1, v) = \varphi(n,v)] \Rightarrow \varphi(n-1,v) = d_e(s,v)$
2) $\exists v \;[\varphi(n-1,v)\ne \varphi(n,v)]\Rightarrow G \;\text{has a negative cycle}$

$$
 \begin{align}
    \varphi(n + 1,v) = \begin{dcases*}
        \varphi(n,v)\\
        \min_{t \in Adj(v)}\{\varphi(n,t) + l(t,v)\}
        \end{dcases*}
  \end{align}
  $$


### **Detecting Negative Cycles**
In order to detect whether a negative cycle exists or not, relax all the edge one more time and if the shortest distance for any node reduces then we can say that a negative cycle exists. In short if we relax the edges $n$ times, and there is any change in the shortest distance of any node between the ${(n-1)}^\text{th}$ and $n^{th}$ relaxation than a negative cycle exists, otherwise not exist.

In other words: after $|V(G)| - 1$ iterations, if $\varphi(k, v)$ continues to decrease when performing additional relaxations, this is an indication that a negative cycle exists.
- If $\varphi(k+1, v) < \varphi(k, v)$ after $k = |V(G)| - 1$, it means there is a path to $v$ that includes a negative weight cycle, and the distance to $v$ can decrease indefinitely.