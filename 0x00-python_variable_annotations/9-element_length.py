#!/usr/bin/env python3
"""
Duck Types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a tuple of elements and lengths
    """
    return [(i, len(i)) for i in lst]
