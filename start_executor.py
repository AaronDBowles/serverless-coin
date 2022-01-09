import asyncio

import executor
import logging

logging.basicConfig(level=logging.DEBUG)
asyncio.run(executor.start())
