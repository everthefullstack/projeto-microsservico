import subprocess, asyncio, platform


async def _config_event_loop_policy():
    if platform.system() == "Windows":
       asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def _run_pytest():
    subprocess.run(["pytest"])

async def _run_test():
    await _config_event_loop_policy()
    await _run_pytest()

if __name__ == "__main__":
    asyncio.run(_run_test())
