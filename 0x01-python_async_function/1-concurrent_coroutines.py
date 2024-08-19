#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of second waited
    """
    waits = [wait_random(max_delay) for _ in range(n)]
    swaits = [await wait for wait in asyncio.as_completed(waits)]
    return swaits
