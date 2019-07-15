from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    # TODO - you fill in here.
    def backTracking(digits, carry):
        if digits == []:
            res.append(carry)
            return

        number = digits[0]
        for j in dic[number]:
            backTracking(digits[1:], carry + j)

    if not phone_number:
        return []
    digits = list(phone_number)
    res = []
    dic = {'0':'0','1':'1', '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    backTracking(digits, '')
    return [i.upper() for i in res]

    # return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
