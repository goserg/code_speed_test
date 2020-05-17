import random
import bisect

import code_speed_test


def insort_test(n: int) -> None:
    lst = []
    for i in range(n):
        bisect.insort(lst, random.random())


def append_sort_test(n: int) -> None:
    lst = []
    for i in range(n):
        lst.append(random.random())
    _ = sorted(lst)


# 1. Create tester object
tester = code_speed_test.Tester()

# 2. Adding tests
# a) creating data list by assigning start (optional stop) and step for range of arguments
tester.add_test_case(insort_test, start=0, step=10000, time_limit=5)

# b) directly passing iterable object of test cases
test_args = [1, 10, 10000, 15000, 100000, 200000, 300000]
tester.add_test_case(append_sort_test, arguments=test_args, time_limit=5)

# 3. Running tests, and plotting the graph
tester.start_computations()
tester.show_plot()
