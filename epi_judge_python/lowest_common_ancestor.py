import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, node0, node1):
    # TODO - you fill in here.
    def helper(tree, node0, node1):
        if not tree:
            return (0, None)
        ansl = helper(tree.left, node0, node1)
        if ansl[0] == 2:
            return ansl
        ansr = helper(tree.right, node0, node1)
        if ansr[0] == 2:
            return ansr
        count = ansl[0]+ ansr[0] + (node0, node1).count(tree)
        return (count, tree if count==2 else None)

    return helper(tree, node0, node1)[1]
    # return None


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
