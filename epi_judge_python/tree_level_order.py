from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


<<<<<<< HEAD
def binary_tree_depth_order(root):
    ans = []
    if not root:
        return []
    level = [root]

    while level:
        ans.append([node.data for node in level])
        level = [i for p in level for i in (p.left, p.right) if i]

    return ans

def binary_tree_depth_order2(root):
    if not root:
        return []


    def traversal(root, level, res):
        if not root:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.data)
        traversal(root.left, level + 1, res)
        traversal(root.right, level + 1, res)


    res = [[]]
    traversal(root, 0, res)
    return res
=======
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # TODO - you fill in here.
    return []
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
