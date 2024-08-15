#!/usr/bin/env python3
"""
String and int/float to typle
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Turns string and int/float to tuple
    """
    return (k, float(v**2))
