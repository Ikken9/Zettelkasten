# Floyd-Warshall Algorithm

Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph. It does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).

We have the next equation:
$$\Psi(\{1, 2, \cdots, k\}, v, w) = \min\{l(P)\}$$

where:

$P$ is the path from $v$ to $w$ that only uses the vertices on $\{1, 2, \cdots, k\}$

