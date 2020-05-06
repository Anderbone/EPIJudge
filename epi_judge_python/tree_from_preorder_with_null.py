import functools
<<<<<<< HEAD
import collections
=======
from typing import List

from binary_tree_node import BinaryTreeNode
>>>>>>> upstream/master
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode

<<<<<<< HEAD
def reconstruct_preorder(preorder):
    
    def helper(plist):
        if plist[-1] is None:
            plist.pop()
            return None
        root = BinaryTreeNode(plist.pop())
        # plist.popleft()
        root.left = helper(plist)
        root.right = helper(plist)
        return root
    preorder.reverse()
    # preorder = collections.deque(preorder)
    return helper(preorder)
=======
def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    return BinaryTreeNode()
>>>>>>> upstream/master


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_with_null.py',
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
