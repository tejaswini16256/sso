import socket
import time
import sys
import logging

# Configure logging with immediate flush
logging.basicConfig(
    level=logging.INFO,
    format='\033[92m%(asctime)s [SERVER] %(message)s\033[0m',  # Green color
    datefmt='%H:%M:%S',
    stream=sys.stdout
)

def start_server():
    print("Starting server...", flush=True)  # Immediate flush
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable socket reuse
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)
    
    logging.info("🚀 Server is running on port 5000")
    sys.stdout.flush()  # Force flush
    
    while True:
        print("\nWaiting for new connections...", flush=True)
        client_socket, address = server_socket.accept()
        logging.info(f"📥 New connection from {address}")
        sys.stdout.flush()  # Force flush
        
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"\n💬 Received: {message}", flush=True)
                response = f"Server received: {message}"
                client_socket.send(response.encode('utf-8'))
                print(f"✅ Sent response for: {message}", flush=True)
                sys.stdout.flush()  # Force flush
        except Exception as e:
            logging.error(f"❌ Error: {e}")
            sys.stdout.flush()
        finally:
            client_socket.close()
            logging.info(f"👋 Connection closed with {address}")
            sys.stdout.flush()

if __name__ == "__main__":
    start_server()