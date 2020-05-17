from __future__ import annotations

import time
from typing import Callable, Tuple, List, Union, Iterable

import matplotlib.pyplot as plt


class _TestCase:
    def __init__(self,
                 func: Callable,
                 start: int,
                 stop: int = None,
                 step: int = 1,
                 time_limit: int = None,
                 ) -> None:
        self.func = func
        self.start = start
        self.stop = stop
        self.step = step
        self.time_limit = time_limit


class _DataTestCase:
    def __init__(self,
                 func: Callable,
                 arguments: Iterable,
                 time_limit: int = None,
                 ) -> None:
        self.func = func
        self.arguments = arguments
        self.time_limit = time_limit


def _compute_range_case(case: _TestCase) -> Tuple[List[int], List[float]]:
    arg = case.start
    arguments: List[int] = []
    times: List[float] = []
    while case.time_limit > 0 if case.time_limit else True:
        if case.stop and arg >= case.stop:
            break
        start_time = time.time()
        case.func(arg)
        time_spent = time.time() - start_time
        times.append(time_spent)
        if case.time_limit:
            case.time_limit -= time_spent
        arguments.append(arg)
        arg += case.step
    return arguments, times


def _compute_args_case(case: _DataTestCase) -> Tuple[List[int], List[float]]:
    arguments: List[int] = []
    times: List[float] = []
    time_spent = 0
    for i in case.arguments:
        if time_spent > case.time_limit:
            break
        start_time = time.time()
        case.func(i)
        time_spent = time.time() - start_time
        times.append(time_spent)
        if case.time_limit:
            case.time_limit -= time_spent
        arguments.append(i)
    return arguments, times


class Tester:
    def __init__(self) -> None:
        self.test_cases: List[Union[_TestCase, _DataTestCase]] = []
        self.results: List[Tuple[List[int], List[float]]] = []

    def add_test_case(self,
                      func: Callable,
                      start: int = 0,
                      stop: int = None,
                      step: int = 1,
                      *,
                      arguments: Iterable = None,
                      time_limit: int = 60,
                      ):
        if arguments:
            self.test_cases.append(_DataTestCase(func, arguments, time_limit))
        else:
            self.test_cases.append(_TestCase(func, start, stop, step, time_limit))

    def start_computations(self) -> None:
        for i in self.test_cases:
            if isinstance(i, _TestCase):
                self.results.append(_compute_range_case(i))
            elif isinstance(i, _DataTestCase):
                self.results.append(_compute_args_case(i))

    def show_plot(self) -> None:
        for case, result in zip(self.test_cases, self.results):
            plt.plot(result[0], result[1], label=case.func.__name__)
        plt.title("CodeSpeedTest")
        plt.xlabel("iterations")
        plt.ylabel("time, sec")
        plt.legend()
        plt.show()
