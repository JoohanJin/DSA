# Graph
***
- A tree is actually a type of graph, but not all of graphs are trees.
    - A tree is a connected graph without cycles.
- A graph is simply a collection of nodes with edges between (some of) them
- Graphs can be either directed or undirected.
    - Directed edges are like a one-way street.
    - Undirected edges are like a two-way street.
- The graph might consist of multiple isolated subgraphs. If there is a path between every pair of vertices, it is called a "connected graph"
- The graph can also have cycles (or not). An "acyclic graph" is one without cycles.

### Adjacency List
- The most common way to represnet a graph.
- Every vertex (or node) stores a list of adjacent vertices.
- In an undirected graph, an edge like (a, b) would be stored twice: once in a's adjacent vertices and once in b's adjacent vertices.

### Adjacency Matrix