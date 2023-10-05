#!/usr/bin/env python3
"""Application of TypeVar"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """Use of TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
