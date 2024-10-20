# Floyd-Warshall Algorithm

Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph. It does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).

We have the next equation:
$$\Psi(\{1, 2, \cdots, k\}, v, w) = \min\{l(P)\}$$

Where $P$ is the path from $v$ to $w$ that only uses the vertices on $\{1, 2, \cdots, k\}$.

Yes, the Bellman equation can be adapted for the **Floyd-Warshall algorithm**, which is used to find the shortest paths between all pairs of vertices in a graph, even for graphs with negative weights (but without negative weight cycles). The Floyd-Warshall algorithm works by iteratively improving estimates of the shortest path between each pair of vertices, considering an increasing number of intermediate vertices.

### **Bellman Equation**

Let $\Psi(i, j, k)$ be the shortest path distance from vertex $i$ to vertex $j$ using only vertices from the set $\{1, 2, \dots, k\}$ as possible intermediate vertices.

The Bellman equation for the Floyd-Warshall algorithm is as follows:

$$
\Psi(i, j, k) = \min\{\Psi(i, j, k-1), \Psi(i, k, k-1) + \Psi(k, j, k-1)\}
$$

Where:
- $\Psi(i, j, k)$ is the shortest distance from vertex $i$ to vertex $j$ considering only intermediate vertices from the set $\{1, 2, \cdots, k\}$.
- $\Psi(i, j, k-1)$ is the shortest distance from $i$ to $j$ without considering vertex $k$ as an intermediate vertex.
- $\Psi(i, k, k-1) + \Psi(k, j, k-1)$ is the path from $i$ to $j$ that goes through vertex $k$, considering only the first $k-1$ vertices as intermediates.

The equation essentially states that the shortest path from vertex $i$ to vertex $j$, considering up to $k$ intermediate vertices, is either:
  - The previously computed shortest path from $i$ to $j$ without using $k$ as an intermediate vertex.
  - A path that goes from $i$ to $j$ through vertex $k$, where the shortest path from $i$ to $k$ and from $k$ to $j$ have already been computed.

**Base Case:**
Initially, when no intermediate vertices are considered (i.e., $k = 0$), the shortest distance between any two vertices $i$ and $j$ is just the direct edge between them, or infinity if no edge exists:

$$
\Psi(i, j, 0) = 
\begin{cases}
0, & \text{if } i = j \\
W(i, j), & \text{if there is an edge } (i, j) \\
\infty, & \text{if there is no edge } (i, j)
\end{cases}
$$

Where $W(i, j)$ is the weight of the edge from $i$ to $j$.