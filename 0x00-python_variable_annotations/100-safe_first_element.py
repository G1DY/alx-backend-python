#!/usr/bin/env python3
"""Augments the function with the correct duck-typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """lists a sequence of objects types of elements are not known"""
    if lst:
        return lst[0]
    else:
        return None
