import socket
import json
import threading
import logging
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='\033[92m%(asctime)s [SERVER] %(message)s\033[0m',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)

class TCPServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logging.info(f"🚀 Server started on {self.host}:{self.port}")
            
            while True:
                client_socket, address = self.server_socket.accept()
                self.clients.append(client_socket)
                logging.info(f"📥 New connection from {address}")
                
                # Start a new thread for each client
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                client_thread.start()
                
        except Exception as e:
            logging.error(f"❌ Server error: {e}")
        finally:
            if self.server_socket:
                self.server_socket.close()

    def handle_client(self, client_socket, address):
        try:
            while True:
                # Receive data from client
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                # Parse JSON data
                try:
                    message = json.loads(data)
                    logging.info(f"📨 Received from {address}: {message}")
                    
                    # Process message based on type
                    response = self.process_message(message)
                    
                    # Send response back to client
                    client_socket.send(json.dumps(response).encode('utf-8'))
                    logging.info(f"📤 Sent to {address}: {response}")
                    
                except json.JSONDecodeError:
                    logging.error(f"❌ Invalid JSON received from {address}")
                    
        except Exception as e:
            logging.error(f"❌ Error handling client {address}: {e}")
        finally:
            client_socket.close()
            self.clients.remove(client_socket)
            logging.info(f"👋 Client {address} disconnected")

    def process_message(self, message):
        """Process received message and return response"""
        msg_type = message.get('type', 'unknown')
        content = message.get('content', '')
        
        response = {
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'type': 'response',
            'original_type': msg_type,
            'content': f"Processed: {content}"
        }
        return response

if __name__ == "__main__":
    server = TCPServer()
    server.start()