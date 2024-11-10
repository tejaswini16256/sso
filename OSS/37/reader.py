import time

def read_from_shared_memory():
    while True:
        try:
            with open("/shared_data/shared_file.txt", "r") as file:
                content = file.read().strip()
                print(f"Reader: Read '{content}' from shared memory.")
        except FileNotFoundError:
            print("Reader: Shared memory file not found.")
        time.sleep(5)  # Read every 5 seconds

if __name__ == "__main__":
    read_from_shared_memory()
