#!/usr/bin/env python3
"""Annotates function’s parameters and return
   values with the appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """lists an iterable sequence and returns a tuple list"""
    return [(i, len(i)) for i in lst]
