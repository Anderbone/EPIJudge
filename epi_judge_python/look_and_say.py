from test_framework import generic_test


def look_and_say(n):

    def helper(str_in):
        res = []
        i = 0
        while i < len(str_in):
            count = 1
            while i+1 < len(str_in) and str_in[i] == str_in[i+1]:
                count += 1
                i += 1
            # print(count)
            res.append(str(count)+str_in[i])
            i += 1
        return ''.join(res)

    s = '1'
    for _ in range(n-1):
        s = helper(s)
    return s

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
