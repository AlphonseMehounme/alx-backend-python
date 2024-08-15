#!/usr/bin/env python3
"""
Union type
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return sum of a mixte list
    """
    return sum(mxd_lst)
