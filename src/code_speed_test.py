from __future__ import annotations

import time
from typing import Callable, Tuple, List

import matplotlib.pyplot as plt


class _TestCase:
    def __init__(self,
                 func: Callable,
                 start: int,
                 stop: int = None,
                 step: int = 1,
                 total_time: int = None,
                 max_time: int = None,
                 ) -> None:
        self.func = func
        self.start = start
        self.stop = stop
        self.step = step
        self.total_time = total_time
        self.max_time = max_time


def _compute_case(case: _TestCase) -> Tuple[List[int], List[float]]:
    arg = case.start
    x: List[int] = []
    y: List[float] = []
    time_spent = 0
    while case.total_time > 0 if case.total_time else True:
        if case.stop and arg >= case.stop:
            break
        if case.max_time and time_spent > case.max_time:
            break
        start_time = time.time()
        case.func(arg)
        time_spent = time.time() - start_time
        y.append(time_spent)
        if case.total_time:
            case.total_time -= time_spent
        x.append(arg)
        arg += case.step
    return x, y


class Tester:
    def __init__(self) -> None:
        self.test_cases: List[_TestCase] = []
        self.results: List[Tuple[List[int], List[float]]] = []

    def add_test_case(self,
                      func: Callable,
                      start: int,
                      stop: int = None,
                      step: int = 1,
                      *,
                      total_time: int = 60,
                      max_time: int = None,
                      ):
        self.test_cases.append(_TestCase(func, start, stop, step, total_time, max_time))

    def start_computations(self) -> None:
        for i in self.test_cases:
            self.results.append(_compute_case(i))

    def show_plot(self) -> None:
        for case, result in zip(self.test_cases, self.results):
            plt.plot(result[0], result[1], label=case.func.__name__)
        plt.title("CodeTestSpeed")
        plt.xlabel("iterations")
        plt.ylabel("time, sec")
        plt.legend()
        plt.show()
