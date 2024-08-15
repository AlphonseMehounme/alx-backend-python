#!/usr/bin/env python3
"""
List int variable Module
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats
    """
    lsum: float = sum(input_list)
    """for x in input_list:
        lsum = lsum + x"""
    return lsum
