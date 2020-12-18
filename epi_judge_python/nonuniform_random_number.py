import collections
import functools
import math
import random
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import run_func_with_retries
from test_framework.test_utils import enable_executor_hook

# def nonuniform_random_number_generation(values, probabilities):
#     # only need to store one side of list, don't need (start, end). could use bisect
#     mydic = {}
#     # for i, vp in enumerate(zip(values,p/robabilities)):
#     for i in range(len(values)):
#         if i == 0:
#             # mydic[values[i]] = [0, probabilities[i]]
#             pre = probabilities[0]
#             mydic[(0, probabilities[i])] = values[i]
#             # print(mydic)
#         else:
#             # mydic[values[i]] = [probabilities[i-1], probabilities[i]]
#             now = pre+probabilities[i]
#             mydic[(pre, now)] = values[i]
#             pre = now
#             # mydic[(probabilities[i-1], probabilities[i]+probabilities[i-1])] = values[i]
#             # print(mydic)
#     # print(mydic)
#     r = random.randrange(0,1)
#     for i in mydic.keys():
#         if r >= i[0] and r < i[1]:
#             return mydic[(i[0], i[1])]
#             # return list(mydic.keys())[list(mydic.values()).index(i[0],i[1])]

def nonuniform_random_number_generation(values: List[int],
                                        probabilities: List[float]) -> int:
    # TODO - you fill in here.
    probsum = list()
    p_sofar = 0
    for p in probabilities:
        p_sofar += p
        probsum.append(p_sofar)
    probsum_value_dic = dict(zip(probsum, values))
    random_p = random.random()
    for p in probsum:
        if random_p < p:
            return probsum_value_dic[p]


@enable_executor_hook
def nonuniform_random_number_generation_wrapper(executor, values,
                                                probabilities):
    def nonuniform_random_number_generation_runner(executor, values,
                                                   probabilities):
        N = 10**6
        result = executor.run(lambda: [
            nonuniform_random_number_generation(values, probabilities)
            for _ in range(N)
        ])

        counts = collections.Counter(result)
        for v, p in zip(values, probabilities):
            if N * p < 50 or N * (1.0 - p) < 50:
                continue
            sigma = math.sqrt(N * p * (1.0 - p))
            if abs(float(counts[v]) - (p * N)) > 5 * sigma:
                return False
        return True

    run_func_with_retries(
        functools.partial(nonuniform_random_number_generation_runner, executor,
                          values, probabilities))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'nonuniform_random_number.py', 'nonuniform_random_number.tsv',
            nonuniform_random_number_generation_wrapper))
