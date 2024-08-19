#!/usr/bin/env python3
"""
Asyncio Basics
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait a random second and return it
    """
    second = random.uniform(0, max_delay)
    await asyncio.sleep(second)
    return second
