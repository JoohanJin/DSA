'''
function: inorder_traversal
l -> c -> r
'''
from data_structure.tree.tree import TreeNode


def in_order_traversal_recur(node: TreeNode):
    if (not node):
        in_order_traversal_recur(node.left)
        visit(node)
        in_order_traversal_recur(node.right)
    return

def in_order_traversal_iter(node: TreeNode):
    stack = []
    solution = []
    dummy = node
    while (dummy or stack):
        if (dummy):
            stack.append(dummy)
            dummy = dummy.left
        elif (stack):
            dummy = stack.pop()
            solution.append(dummy.val)
            dummy.right
    return solution

'''
function: preorder_traversal
c -> l -> r
'''
def pre_order_traversal_recur(node: TreeNode):
    if (not node):
        visit(node)
        in_order_traversal_recur(node.left)
        in_order_traversal_recur(node.right)
    return

def pre_order_traversal_iter(node: TreeNode):
    stack = []
    solution = []
    stack.append(node)
    solution.append(node.val)

    dummy = node.left
    while (dummy or stack):
        if dummy:
            solution.append(dummy.val)
            stack.append(dummy)
            dummy = dummy.left
        elif stack:
            dummy = stack.pop().right
    return solution


'''
function: postorder_traversal
l -> r -> c
'''
def post_order_traversal_recur(node: TreeNode):
    if (not node):
        post_order_traversal_recur(node.left)
        post_order_traversal_recur(node.right)
        visit(node)
    return

def post_order_traversal_recur(node: TreeNode):
    # stack = []
    # solution = []
    # stack.append(node)
    # dummy = node
    # while (dummy or stack):
    #     dummy = stack.pop() if (stack) else  None
    #     if dummy:
    #         solution.insert(0, dummy.value)
    #         if dummy.left: stack.append(dummy.left)
    #         if dummy.right: stack.append(dummy.right)
    # return
    # TODO: find the better method for post_order_traversal
    raise NotImplementedError
