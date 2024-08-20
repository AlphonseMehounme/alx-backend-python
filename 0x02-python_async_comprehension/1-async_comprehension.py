#!/usr/bin/env python3
"""
Async comprehension
"""
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Async comprehension with async generator
    """
    num = []
    async for i in async_generator():
        num.append(i)
    return num
