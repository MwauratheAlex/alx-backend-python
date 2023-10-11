#!/usr/bin/env python3
"""This modulw contains the function wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random that waits for a random delay between 0 and max_delay"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
