from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


<<<<<<< HEAD
def is_symmetric(tree):
    if not tree:
        return True

    def helper(l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.data != r.data:
            return False
        return helper(l.left, r.right) and helper(l.right, r.left)

    return helper(tree.left, tree.right)
=======
def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    return True
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
