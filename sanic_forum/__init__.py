import asyncio
import os

# from dotenv import load_dotenv

# load_dotenv()

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
