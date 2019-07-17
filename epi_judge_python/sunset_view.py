from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    # TODO - you fill in here.
    # dic = {}
    stack = []

    for i, h in enumerate(reversed(sequence)):
        if not stack:
            stack.append((i, h))
            # dic[len(sequence)-1-i] = h
        elif h <= stack[-1][1]:
            continue
        else:
            stack.append((i,h))
    return [len(sequence)-1-i[0] for i in stack]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
