import asyncio

import full_node
import logging

logging.basicConfig(level=logging.DEBUG)
asyncio.run(full_node.start())
