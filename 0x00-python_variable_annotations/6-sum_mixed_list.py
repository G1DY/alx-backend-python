#!/usr/bin/env python3
"""function sum_mixed_list that sums a mixed list and returns a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums a mixed list and returns them as float"""
    return sum(mxd_lst)
