#!/usr/bin/env python3
"""
Mapping Typing
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return any type
    """
    if key in dct:
        return dct[key]
    else:
        return default
