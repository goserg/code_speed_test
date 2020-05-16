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


tester = code_speed_test.Tester()
tester.add_test_case(insort_test, 0, step=10000)
tester.add_test_case(append_sort_test, 0, step=10000)
tester.start_computations()
tester.show_plot()
