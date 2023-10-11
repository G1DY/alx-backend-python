#!/usr/bin/env python3
"""collects 10 random numbers using an async comprehensing over async_generator
   then return the 10 random numbers.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """creates a list of 10 float numbers from the function 0-async_generator
    """
    return[number async for number in async_generator()]


if __name__ == "__main__":
    asyncio.run()
