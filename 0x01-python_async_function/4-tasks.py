#!/usr/bin/env python3
"""
Concurrent coroutines
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of second waited
    """
    waits = [task_wait_random(max_delay) for _ in range(n)]
    swaits = [await wait for wait in asyncio.as_completed(waits)]
    return swaits
