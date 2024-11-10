import socket
import time
import sys
import logging
from datetime import datetime

# Configure logging with colors and formatting
logging.basicConfig(
    level=logging.INFO,
    format='\033[94m%(asctime)s [CLIENT] %(message)s\033[0m',  # Blue color
    datefmt='%H:%M:%S',
    stream=sys.stdout
)

def format_message(msg):
    """Add timestamp to message"""
    timestamp = datetime.now().strftime('%H:%M:%S')
    return f"[{timestamp}] {msg}"

def start_client():
    logging.info("🔌 Initializing client...")
    sys.stdout.flush()
    
    time.sleep(5)  # Wait for server to start
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connection loop with fancy status messages
    logging.info("🔍 Looking for server...")
    while True:
        try:
            client_socket.connect(('server', 5000))
            break
        except socket.error:
            print("⏳ Waiting for server connection...", flush=True)
            time.sleep(2)
    
    logging.info("✨ Connected to server successfully!")
    sys.stdout.flush()
    
    try:
        for i in range(5):
            # Prepare and send message
            message = f"Message {i+1} from client"
            logging.info(f"📤 Sending: {message}")
            client_socket.send(message.encode('utf-8'))
            
            # Receive and display response
            response = client_socket.recv(1024).decode('utf-8')
            logging.info(f"📥 Received: {response}")
            
            # Visual separator for better readability
            print("-" * 50, flush=True)
            sys.stdout.flush()
            time.sleep(1)
            
    except ConnectionResetError:
        logging.error("❌ Server connection was lost!")
    except ConnectionRefusedError:
        logging.error("❌ Server refused connection!")
    except Exception as e:
        logging.error(f"❌ Unexpected error: {str(e)}")
    finally:
        client_socket.close()
        logging.info("👋 Connection closed")
        
    logging.info("✅ Client session completed")
    sys.stdout.flush()

def display_banner():
    banner = """
    ╔══════════════════════════════╗
    ║      Client Started      ║
    ╚══════════════════════════════╝
    """
    print('\033[95m' + banner + '\033[0m', flush=True)  # Purple color

if __name__ == "__main__":
    display_banner()
    start_client()