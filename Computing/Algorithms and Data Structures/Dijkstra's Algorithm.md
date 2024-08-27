# Dijkstra's Algorithm

Is an algorithm for finding the shortest paths between nodes in a weighted graph, which may represent, for example, road networks.

The algorithm uses a ***min-priority queue*** data structure for selecting the shortest paths known so far.

## Algorithm

Let us choose a **starting node** and for convenience name it ***S***, and let the **distance of node _N_** be the distance from *S* to *N*. Dijkstra's algorithm will initially start with infinite distances and will try to improve them step by step.

1. Mark all nodes as unvisited. Create a **set** of all the unvisited nodes called the _unvisited set_.
2. Assign to every node a _distance from start_ value: for the starting node **S**, it is **zero**, and for all other nodes, it is **infinity**, since initially no path is known to these nodes. During execution of the algorithm, the distance of a node _N_ is the length of the shortest path discovered so far between S and *N*.
3. From the unvisited set, select the current node to be the one with the smallest finite distance; initially, this will be the starting node, which has distance zero. If the unvisited set is empty, or contains only nodes with infinite distance (which are unreachable), then the algorithm terminates by going to step 6. If we are only concerned about the path to a target node, we may terminate here if the current node is the target node. Otherwise, we can continue to find the shortest paths to all reachable nodes.
4. For the current node, consider all of its unvisited neighbors and update their distances through the current node; compare the newly calculated distance to the one currently assigned to the neighbor and assign it the smaller one. For example, if the current node _A_ is marked with a distance of 6, and the edge connecting it with its neighbor _B_ has length 2, then the distance to _B_ through _A_ is 6 + 2 = 8. If B was previously marked with a distance greater than 8, then update it to 8 (the path to B through A is shorter). Otherwise, keep its current distance (the path to B through A is not the shortest).
5. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. This is so that a visited node is never checked again, which is correct because the distance recorded on the current node is minimal (as ensured in step 3), and thus final. Go back to step 3.
6. Once the loop exits (steps 3–5), every visited node will contain its shortest distance from the starting node.


## Mathematical Model

#### Initialization
$X = [s]$
$\phi[s] = 0$

#### Execution
List all the $U_i, V_i$ with $U_i\in X, V_i\notin X$:

$\begin{array}{c} (U_i, V_i) \\ \vdots \\ (U_n, V_n) \end{array}$


###### Now calculate:
$\begin{array}{c} l(U_i, V_i) + \phi(U_i) \\ \vdots \\ l(U_n, V_n) + \phi(U_n) \end{array}$

###### Take the minimum:
$l(U^*, V^*) + \phi(U^*) = min \{l(U_i, V_i) + \phi(U_i)\}$

###### Save the vertex:
$X \leftarrow X \bigcup \{V^*\}$

###### Save the best path:
$\phi(V^*) := l(U^*, V^*) + \phi(U^*)$


## Code Implementation (Rust)

##### Using a heap
```
pub fn dijkstra_heap(&mut self, start: Vertex) {  
    let mut distances: HashMap<VertexId, u32> = HashMap::new();  
    let mut visited: HashSet<VertexId> = HashSet::new();  
  
    let mut priority_queue = BinaryHeap::new();  
  
    distances.insert(start.id.clone(), 0);  
    priority_queue.push(State { vertex: start.id, cost: 0 });  
  
    while let Some(State { vertex: current_vertex, cost: current_distance }) = priority_queue.pop() {  
        if !visited.insert(current_vertex) {  
            continue;  
        }  
  
        println!("Visited {:?}", visited);  
  
        if let Some(v) = self.vertices.get(&current_vertex) {  
            for neighbor in &v.edges {  
                if let Some(next) = self.vertices.get(&neighbor.to) {  
                    let distance = current_distance + neighbor.weight;  
  
                    if distance < *distances.get(&neighbor.to).unwrap_or(&u32::MAX) {  
                        distances.insert(neighbor.to.clone(), distance);  
                        priority_queue.push(State { vertex: next.id, cost: distance });  
                    }  
                }  
            }  
        }  
    }  
}
```

##### Without using a heap
```
pub fn dijkstra_no_heap(&mut self, start: Vertex) {  
    let mut distances: HashMap<VertexId, u32> = HashMap::new();  
    let mut visited: HashSet<VertexId> = HashSet::new();  
  
    distances.insert(start.id.clone(), 0);  
  
    let mut current_vertex = start.id.clone();  
    let graph_len = self.vertices.keys().len();  
  
    while visited.len() < graph_len {  
        visited.insert(current_vertex);  
        println!("Visited {:?}", visited);  
        let current_distance *distances.get(&current_vertex).unwrap_or(&u32::MAX);  
  
        if let Some(v) = self.vertices.get(&current_vertex) {  
            for neighbor in &v.edges {  
                let distance = current_distance + neighbor.weight;  
  
                if distance < *distances.get(&neighbor.to).unwrap_or(&u32::MAX) {  
                    distances.insert(neighbor.to, distance);  
                }  
            }  
        }  
  
        let next_vertex = self.vertices  
            .iter()  
            .filter(|(_, v)| !visited.contains(&v.id))  
            .min_by_key(|(_, v)| distances.get(&v.id).unwrap_or(&u32::MAX))  
            .map(|(_, v)| v.clone());  
  
        match next_vertex {  
            Some(v) => current_vertex = v.id,  
            None => break,  
        }  
    }  
}
```

## Pseudocode

##### Using a heap
```pseudo
	\begin{algorithm}
	\caption{Dijkstra(Grafo \(G\), nodo\_partida \(s\))}
	\begin{algorithmic}
	\For{cada \(u \in V[G]\)}
		\State distancia[\(u\)] = INFINITO 
		\State padre[\(u\)] = NULL 
		\State visto[\(u\)] = \textbf{false}
	\EndFor
	\State distancia[\(s\)] = 0 
	\State adicionar(cola, (\(s\), distancia[\(s\)]))
	\While{cola no es vacía} 
		\State \(u\) = extraer\_mínimo(cola) 
		\State visto[\(u\)] = \textbf{true} 
		\For{cada \(v \in adyacencia[u]\)} 
			\If{no visto[\(v\)]} 
				\If{distancia[\(v\)] > distancia[\(u\)] + peso(\(u\), \(v\))} 
				\State distancia[\(v\)] = distancia[\(u\)] + peso(\(u\), \(v\)) 
				\State padre[\(v\)] = \(u\) \State adicionar(cola, (\(v\), distancia[\(v\)])) 
			\EndIf 
		\EndIf 
		\EndFor 
	\EndWhile
	\end{algorithmic}
	\end{algorithm}
```

##### Without using a heap
```pseudo
	\begin{algorithm}
	\caption{Dijkstra(Grafo \(G\), nodo\_partida \(s\))} 
	\begin{algorithmic}
	\State // Usaremos un vector para guardar las distancias del nodo partida al resto 
	\State \textbf{entero} distancia[n] 
	\State // Inicializamos el vector con distancias iniciales 
	\State \textbf{booleano} visto[n] 
	\State // Vector de booleanos para controlar los vértices de los que ya tenemos la distancia mínima 
	\For{cada \(w \in V[G]\)} 
		\If{no existe arista entre \(s\) y \(w\)} 
			\State distancia[\(w\)] = Infinito // puedes marcar la casilla con un -1 por ejemplo 
		\Else 
			\State distancia[\(w\)] = peso(\(s\), \(w\)) 
		\EndIf 
	\EndFor 
	\State distancia[\(s\)] = 0 
	\State visto[\(s\)] = \textbf{cierto} 
	\State // \(n\) es el número de vértices que tiene el Grafo 
	\While{no\_estén\_vistos\_todos} 
		\State vértice = tomar\_el\_mínimo\_del\_vector distancia y que no esté visto; 
		\State visto[vértice] = \textbf{cierto}; 
		\For{cada \(w \in sucesores(G, vértice)\)} 
			\If{distancia[\(w\)] > distancia[vértice] + peso(vértice, \(w\))} 
				\State distancia[\(w\)] = distancia[vértice] + peso(vértice, \(w\)) 
			\EndIf 
		\EndFor 
	\EndWhile

	\end{algorithmic}
	\end{algorithm}
```

