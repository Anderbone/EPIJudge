from test_framework import generic_test


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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
