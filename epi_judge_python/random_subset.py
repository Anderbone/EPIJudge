import functools
<<<<<<< HEAD
import random
=======
from typing import List
>>>>>>> upstream/master

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


<<<<<<< HEAD
def random_subset(n, k):
    A = list(range(n))

    for i in range(k):
        r = random.randrange(i, n)
        A[i], A[r] = A[r], A[i]
# A[:] = random.sample(A, k)
    return A[:k]
=======
def random_subset(n: int, k: int) -> List[int]:
    # TODO - you fill in here.
    return []
>>>>>>> upstream/master


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
