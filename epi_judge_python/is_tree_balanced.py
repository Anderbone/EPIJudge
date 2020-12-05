from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# def is_balanced_binary_tree(tree):
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
    # TODO - you fill in here.
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
            # if not level:
            #     return 0
            height += 1
            level = [i for n in level for i in (n.left, n.right) if i]
        return height

    # post order? left, right, root. once not balanced found, return false
    def post_order(root):
        post_order(root.left)
        post_order(root.right)
        print(root)

    level = [tree]
    if not level:
        return True
    while level:
        for node in level:
            if not node:
                return True
            if abs(height2(node.left) - height2(node.right)) > 1:
                return False
        level = [i for n in level for i in (n.left, n.right) if i]

    # stack = []
    # while True:
    #     while tree:
    #         stack.append(tree)
    #         tree = tree.left
    #     if not stack:
    #         return True
    #     node = stack.pop()
    #     if abs(height(node.left) - height(node.right)) > 1:
    #         return False
    #     tree = node.right

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
