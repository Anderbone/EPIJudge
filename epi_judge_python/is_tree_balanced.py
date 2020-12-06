import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# def is_balanced_binary_tree(tree):   # old
#     def height(root):
#         if not root:
#             return 0
#         lh = height(root.left)
#         rh = height(root.right)
#         return 1 + max(lh, rh)
#
#     # def helper(root):
#     #     if not root:
#     #         return True
#     #     if abs(height(root.left) - height(root.right)) <= 1:
#     #         return True
#     #     return False
#     def helper(root):
#         if not root:
#             return True
#         if abs(height(root.left) - height(root.right)) > 1:
#             return False
#         return True
#
#     stack = []  # iterative in-order traversal.
#     while True:
#         while tree:
#             stack.append(tree)
#             tree = tree.left
#         if not stack:
#             return True
#         node = stack.pop()
#         if not helper(node):
#             return False
#         tree = node.right

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    NodeStatus = collections.namedtuple('NodeStatus',('isBalanced','height'))
    def check_balanced(tree):
        if not tree:
            return NodeStatus(True, -1)

        leftStatus = check_balanced(tree.left)
        if not leftStatus.isBalanced:
            return NodeStatus(False, 0)

        rightStatus = check_balanced(tree.right)
        if not rightStatus.isBalanced:
            return NodeStatus(False, 0)

        isBalanced = abs(leftStatus.height - rightStatus.height) <= 1
        height = 1 + max(leftStatus.height, rightStatus.height)
        return NodeStatus(isBalanced, height)

    return check_balanced(tree).isBalanced

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def height(root):
        if not root:
            return 0
        lh = height(root.left)
        rh = height(root.right)
        return 1 + max(lh, rh)

    def height2(root):
        if not root:
            return 0
        height = 0
        level = [root]
        while level:
            height += 1
            level = [i for n in level for i in (n.left, n.right) if i]
        return height

    level = [tree]
    if not level:
        return True
    while level:
        for node in level:
            if not node:
                return True
            if abs(height2(node.left) - height2(node.right)) > 1:
            # if abs(height(node.left) - height(node.right)) > 1:
                return False
        level = [i for n in level for i in (n.left, n.right) if i]

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
