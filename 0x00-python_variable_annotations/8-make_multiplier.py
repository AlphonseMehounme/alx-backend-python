#!/usr/bin/env python3
"""
Function return
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a multiplier
    """
    def multip(num: float) -> float:
        """
        Multiply num by multiplier
        """
        return num * multiplier
    return multip
