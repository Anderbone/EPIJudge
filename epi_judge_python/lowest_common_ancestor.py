import collections
import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
#         node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
#     # TODO - you fill in here.
#     def helper(tree, node0, node1):
#         if not tree:
#             return (0, None)
#         ansl = helper(tree.left, node0, node1)
#         if ansl[0] == 2:
#             return ansl
#         ansr = helper(tree.right, node0, node1)
#         if ansr[0] == 2:
#             return ansr
#         count = ansl[0]+ ansr[0] + (node0, node1).count(tree)
#         return (count, tree if count==2 else None)
#
#     return helper(tree, node0, node1)[1]
    # return None
def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    Num_nodes_and_tree = collections.namedtuple('Num_nodes_and_tree',('num_nodes','tree'))
    def lca_helper(tree, node0, node1):
        if not tree:
            return Num_nodes_and_tree(0, None)
        left_res = lca_helper(tree.left, node0, node1)
        if left_res.num_nodes == 2:
            return left_res
        right_res = lca_helper(tree.right, node0, node1)
        if right_res.num_nodes == 2:
            return right_res

        num_nodes = left_res.num_nodes + right_res.num_nodes + (node0, node1).count(tree)
        return Num_nodes_and_tree(num_nodes, tree if num_nodes == 2 else None)

    return lca_helper(tree, node0, node1).tree

@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
