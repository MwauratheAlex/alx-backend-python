#!/usr/bin/env python3
"""This module contains the coroutine async_comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers."""
    results = [result async for result in async_generator()]
    return results
