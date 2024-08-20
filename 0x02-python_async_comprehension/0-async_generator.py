#!/usr/bin/env python3
"""
Generator
"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loop 10 times and yield a number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
