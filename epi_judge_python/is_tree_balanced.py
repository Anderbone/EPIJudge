from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


<<<<<<< HEAD
def is_balanced_binary_tree(tree):
    def height(root):
        if not root:
            return 0
        lh = height(root.left)
        rh = height(root.right)
        return 1+max(lh, rh)
=======
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    return True
>>>>>>> upstream/master

    def helper(root):
        if not root:
            return True
        if abs(height(root.left) - height(root.right)) <= 1:
            return True
        return False

    stack = []  # iterative in-order traversal.
    while True:
        while tree:
            stack.append(tree)
            tree = tree.left
        if not stack:
            return True
        node = stack.pop()
        if not helper(node):
            return False
        tree = node.right

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
