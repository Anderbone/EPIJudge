import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None  # Populates this field.


def construct_right_sibling(tree):

    def levelOrder(root):
        ans = []
        if not root:
            return []
        level = [root]
        while level:
            ans.append([node.data for node in level])
            level = [i for p in level for i in (p.left, p.right) if i]
        return ans

    res = levelOrder(tree)

    for level, row in enumerate(res):
        for count, each in enumerate(row):
            if count == 2 ** level - 1:
                each.next = None
            else:
                # while(each is not None):
                each.next = row[count + 1]
    return tree



def traverse_next(node):
    while node:
        yield node
        node = node.next
    raise StopIteration


def traverse_left(node):
    while node:
        yield node
        node = node.left
    raise StopIteration


def clone_tree(original):
    if not original:
        return None
    cloned = BinaryTreeNode(original.data)
    cloned.left, cloned.right = clone_tree(original.left), clone_tree(
        original.right)
    return cloned


@enable_executor_hook
def construct_right_sibling_wrapper(executor, tree):
    cloned = clone_tree(tree)

    executor.run(functools.partial(construct_right_sibling, cloned))

    return [[n.data for n in traverse_next(level)]
            for level in traverse_left(cloned)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_right_sibling.py",
                                       'tree_right_sibling.tsv',
                                       construct_right_sibling_wrapper))
