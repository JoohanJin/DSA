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