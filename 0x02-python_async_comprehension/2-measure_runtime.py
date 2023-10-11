#!/usr/bin/env python3
"""This module contains the function measure_runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension four times in parallel
    using asyncio.gather.
    Measures the total runtime and return it."""
    start_time = time.time()

    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)

    time_taken = time.time() - start_time

    return time_taken
