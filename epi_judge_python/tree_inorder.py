from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.

    res, stack = [], []

    while True:
        while tree:
            stack.append(tree)
            tree = tree.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.data)
        tree = node.right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
