# Trees and Graphs
***

### Types of Trees
A tree is a data structure composed of nodes:
- each tree has a root node, (Actually, this is not strictly necessary in graph theory, but it's usually how we use trees in programmin and especially programming interview)
- the root node has 0 or more child nodes
- each child node has 0 or more child nodes and so on.

The tree cannot contain cycles. The nodes may or may not be in a particualr order, they could have any data type as values.
They may or may not have links back to their parent nodes.

#### Trees vs Binary Trees
A binary tree is a tree in which each node has up to two children.
A node is called a "leaf" node if it has no children.

#### Binary Search Tree
A binary tree in which every node fits a specific ordering property:
- all left descendents <= n < all right descendents. This must be true for each node n.

#### Balanced Tree
- the balancing a tree does not necessarily mean that the left and right subtrees are exactly the same size.
- It's balanced enough to ensure O(log n) times for insert and find, but it's not necesarily as balanced is it could be.

Two common tuypes of balanced trees are red-black trees and AVL trees.

#### Complete Binary Trees
- a binary tree in which every level of the tree is fully filled, except for perhaps the last level.
- to the extent that the last level is filled, it is filled left to right

#### Full Binary Trees
- a binary tree in which every node has either zero or two children. i.e., no nodes have only one child

#### Perfect Binary Trees
- a binary tree which is both complete and full.
    - All leaf nodes will be at the same level
    - This level has the maximum number of nodes.

### Binary Tree Traversal
#### In-Order Traversal
- left -> center -> right

#### Pre=Order Traversal
- center -> left -> right

#### Post-Order Traversal
- left -> right -> center

***
### Heap (Min-Heap and Max-Heap)
- a complete binary tree (totally filled other than the rightmost elements on the last level) where each node is smaller (or larger) than its children.
- The root is the minimum, for min-heap, or the maximum, for max-heap.
#### Key Operations (only consider min-heap in this document, although max-heap operations are equivalent, except that the order is decsending order)
- Insert
    - always start by inserting the element at the bottom, i.e., insert new element at the right most spot so as to maintain the complete tree property.
    - Now, fix the tree swapping the new element with its parent, until we find an appropriate sopt for the element, essentially bubble up the minimum element.
- Extract Minimum Element
    - it is always easy to find the minimum element, which is always at the top.
    - How to remove?
    - We remove the minimum element and swap it with the last element in the heap (the bottommost, rightmost element)
    - Then bubble down the element, swapping it with one of its children until the min-heap property is restored.
        - Do we swap the left child or the right child?
        - Although there is no inherent ordering between the left and right element, the tree needs to take the smaller one in order to maintain the min-heap ordering.
***
### Tries
- A variant of an n-ary tree in which characters are stored at each node.
- Each path down the tree may represent a word.
- The '*' nodes (null nodes) are often used to indicate complete words.

### Graph
- A collection of nodes with edges between (some of) them
    - a tree is a connected graph without cycles
- Graphs can be either directed or undirected. While directed edges are like a one-way street, undirected edges are like a two-way street.
- The graph might consist of multiple isolated subgraphs. If there is a path between every pair of vertices, it is called a "connected graph"
- The graph can also have cycles (or not). An "acyclic graph" is one without cycles.

#### Adjacency List
- The most common way to represent a graph
- Every vertex (or nodes) stores a list of adjacnet vertices.
- In an undirected graph, an edge, e.g., (a, b), would be stored twice: once in a's adjacent vertices and once in b's adjacent vertices.

#### Adjacency Matrix
- an N*N boolean matrix, 2d-array, where N is the number of nodes, where a true value at matrix[i][j] indicates an edge from node i to node j.
    - or we can use 0s and 1s
- In an undirected graph, an adjacency matrix will be symmetric
- In a directed graph, it will not (necessarily) be.

### Graph Search
#### BFS (Breadth-First Search)
- Using queue
- start at the root (or another arbitrarily selected node) and explore each neighbor before going on to any of their children.
    - traverse all the neighbors first.
- If we want to find the shortest path (or just any path) between two nodes, BFS is more preferred

#### DFS (Depth-Firt Search)
- Using recursion (or stack)
- start at the root (or another arbitrarily selected node) and explore each branch completely before moving on to the next branch.
    - Traverse one complete branch
- Pre-order, post-order, in-order traversal
- Often preferred if we want to visit every node in the graph. Both of them are working fine, but DFS is simpler.