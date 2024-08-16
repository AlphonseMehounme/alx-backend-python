#!/usr/bin/env python3
"""
Checking Types with mypy
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    zoom arrays
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
