#!/usr/bin/python3
"""a coroutine that takes no argument"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10times each time asynchronously waits 1 second
       then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
