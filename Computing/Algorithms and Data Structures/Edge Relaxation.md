# Edge Relaxation

In the context of **Dijkstra's Algorithm** and **Bellman-Ford Algorithm**, **relaxation** is a key concept that involves updating the shortest known path to a vertex. It works by checking if a shorter path can be found to a given vertex through one of its neighboring vertices. If a shorter path is found, the algorithm updates the current shortest path estimate.

### **Relaxation in Dijkstra's Algorithm**
In Dijkstra’s algorithm, for each vertex $v$, the algorithm repeatedly checks whether the shortest known path to $v$ can be improved by going through a neighboring vertex $u$. If the distance to $v$ through $u$ is shorter than the current known distance to $v$, the distance is updated.

Mathematically, if the current known shortest distance to vertex $v$ is $d(v)$, and there's an edge from $u$ to $v$ with weight $w(u, v)$, the algorithm checks if:

  $$d(v) > d(u) + w(u, v)$$

If this condition holds, the distance to $v$ is updated to:
  $$d(v) = d(u) + w(u, v)$$
  
  
### **Relaxation in Bellman-Ford Algorithm**
In the Bellman-Ford algorithm, relaxation is done in a similar way. However, unlike Dijkstra's algorithm, which uses a priority queue to efficiently find the next closest vertex, Bellman-Ford repeatedly relaxes all the edges. It performs this relaxation process $V-1$ times (where $V$ is the number of vertices in the graph), ensuring that the shortest paths are found even if negative weights are involved.

After all $V-1$ iterations of relaxation, the algorithm does one additional pass to check for negative weight cycles. If any distance can still be improved after $V-1$ iterations, a negative weight cycle exists.

### Key Differences:
In **Dijkstra's Algorithm**, relaxation is performed in a specific order determined by the shortest discovered paths (it assumes non-negative weights).
In **Bellman-Ford Algorithm**, all edges are relaxed in every iteration, making it suitable for graphs with negative weights.
