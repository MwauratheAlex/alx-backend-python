#!/usr/bin/env python3
"""This module contains the function measure_time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay),
    returns total_time / n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    time_taken = time.time() - start_time

    return time_taken / n
