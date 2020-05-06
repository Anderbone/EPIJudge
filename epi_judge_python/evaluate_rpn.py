from test_framework import generic_test


<<<<<<< HEAD
def evaluate(tokens):
    tokens = tokens.split(',')
    if not tokens:
        return
    stack = []

    for i in tokens:
        if i.lstrip('-').isdigit():
            stack.append(int(i))

        else:
            right = stack.pop()
            left = stack.pop()
            if i == '+':
                temp = left + right
            elif i == '-':
                temp = left - right
            elif i == '*':
                temp = left * right
            elif i == '/':
                temp = int(left / right)
            stack.append(temp)

    return stack[0]
=======
def evaluate(expression: str) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
