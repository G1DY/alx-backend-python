#!/usr/bin/env python3
"""Application of mypy"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """use of mypy"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
        ]
    return list(zoomed_in)
