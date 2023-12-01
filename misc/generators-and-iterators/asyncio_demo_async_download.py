
import time
import asyncio

async def download_file_async(file_number):
    print(f"Downloading file {file_number} asynchronously...")
    await asyncio.sleep(2)  # Simulating a download delay
    print(f"File {file_number} downloaded asynchronously.")

async def main_async():
    await asyncio.gather(
        download_file_async(1),
        download_file_async(2),
        download_file_async(3)
    )

async def run_async():
    start_time = time.time()
    await main_async()
    end_time = time.time()
    print(f"Asynchronous download time: {end_time - start_time} seconds")

# Running the asynchronous function
asyncio.run(run_async())
