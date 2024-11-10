import socket
import json
import time
import logging
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='\033[94m%(asctime)s [CLIENT] %(message)s\033[0m',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)

class TCPClient:
    def __init__(self, host='server', port=5000):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Try to connect to server
        while True:
            try:
                logging.info(f"🔌 Attempting to connect to {self.host}:{self.port}")
                self.socket.connect((self.host, self.port))
                logging.info("✨ Connected successfully!")
                break
            except socket.error:
                logging.warning("⏳ Server not available, retrying in 2 seconds...")
                time.sleep(2)

    def send_message(self, message_type, content):
        if not self.socket:
            raise Exception("Not connected to server")

        message = {
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': message_type,
            'content': content
        }

        try:
            # Send message
            self.socket.send(json.dumps(message).encode('utf-8'))
            logging.info(f"📤 Sent: {message}")

            # Receive response
            response = self.socket.recv(1024).decode('utf-8')
            response_data = json.loads(response)
            logging.info(f"📥 Received: {response_data}")
            
            return response_data

        except Exception as e:
            logging.error(f"❌ Error in communication: {e}")
            return None

    def close(self):
        if self.socket:
            self.socket.close()
            logging.info("👋 Connection closed")

def run_client_demo():
    client = TCPClient()
    
    try:
        # Connect to server
        client.connect()

        # Send different types of messages
        message_types = ['greeting', 'data', 'query', 'update', 'status']
        for i, msg_type in enumerate(message_types):
            content = f"Test message {i+1} with type '{msg_type}'"
            response = client.send_message(msg_type, content)
            print("-" * 50)
            time.sleep(1)

    except Exception as e:
        logging.error(f"❌ Error in demo: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    run_client_demo()