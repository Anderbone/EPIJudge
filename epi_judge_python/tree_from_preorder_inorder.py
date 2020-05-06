from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

<<<<<<< HEAD
def binary_tree_from_preorder_inorder(preorder, inorder):
    if not inorder:
            return None
    d=len(inorder)-1
    i,j=0,d
    preorder.reverse()
    map_inorder={val:index for index,val in enumerate(inorder)}

    def recur(low,high):
        if low>high:
            return None
        root = BinaryTreeNode(preorder.pop())
        mid = map_inorder[root.data]
        root.left = recur(low,mid-1)
        root.right = recur(mid+1,high)
        return root

    return recur(0,d)
=======
def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    return BinaryTreeNode()
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
