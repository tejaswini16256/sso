import time
from datetime import datetime

def write_to_shared_memory():
    counter = 1
    while True:
        message = f"Message {counter} from Writer at {datetime.now()}"
        with open("/shared_data/shared_file.txt", "w") as file:
            file.write(message)
        print(f"Writer: Written '{message}' to shared memory.")
        counter += 1
        time.sleep(5)  # Write every 5 seconds

if __name__ == "__main__":
    write_to_shared_memory()
