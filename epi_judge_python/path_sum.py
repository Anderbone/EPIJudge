from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    # TODO - you fill in here.

    #
    # def helper(root, pathv, target, flag):
    #     if flag == 1:
    #         return True
    #     if not root:
    #         return
    #     print(pathv)
    #
    #     helper(root.left, pathv, target, flag)
    #     helper(root.right, pathv, target, flag)
    #     pathv = pathv + root.data
    #     if pathv == target:
    #         flag = 1
    #     return
    #
    # helper(tree, 0, remaining_weight, 0)

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
