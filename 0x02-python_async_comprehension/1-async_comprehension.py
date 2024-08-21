#!/usr/bin/env python3
"""
Async comprehension
"""
import asyncio
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None][]:
    """
    Async comprehension with async generator
    """
    return [i async for i in async_generator()]
