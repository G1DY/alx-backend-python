#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier as argument
   and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a callable function that returns a float"""
    def new_function(x: float) -> float:
        """new function to test"""
        return x * multiplier
    return new_function
