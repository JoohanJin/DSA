class Node():
    def __init__(self):
        self.neighbors: list[Node] = []
        self.visited = False

    def visited(self):
        # mark this node as visited
        self.visited = True
        return
    
def visit(node: Node):
    # do something with the data in the node
    return
'''
function name: search
task: Implemented DFS (Depth-First Search)
'''
def search(root: Node):
    if (not root): return

    visit(root)

    root.visited()

    for neighbor in root.neighbors:
        if (neighbor.visited == False):
            search(neighbor)

'''
function name: search
task: Implemented BFS (Breadth-First Search)
'''
import queue
def search(root: Node):
    q: queue.Queue = queue.Queue()
    raise NotImplementedError