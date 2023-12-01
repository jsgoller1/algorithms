
import time

def download_file(file_number):
    print(f"Downloading file {file_number}...")
    time.sleep(2)  # Simulating a download delay
    print(f"File {file_number} downloaded.")

def main_sync():
    for i in range(1, 4):
        download_file(i)

start_time = time.time()
main_sync()
end_time = time.time()
print(f"Synchronous download time: {end_time - start_time} seconds")
