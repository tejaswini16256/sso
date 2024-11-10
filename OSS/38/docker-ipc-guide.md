# Docker Inter-Process Communication Guide
## Using Python Socket Programming with Docker

### 1. Project Structure
```
docker-ipc-project/
│
├── server.py           # Server application code
├── client.py           # Client application code
├── Dockerfile.server   # Server container configuration
├── Dockerfile.client   # Client container configuration
├── docker-compose.yml  # Docker compose configuration
└── README.md          # Project documentation
```

### 2. Application Files

#### 2.1. Server Application (server.py)
```python
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
    print("Starting server...", flush=True)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)
    
    logging.info("🚀 Server is running on port 5000")
    sys.stdout.flush()
    
    while True:
        print("\nWaiting for new connections...", flush=True)
        client_socket, address = server_socket.accept()
        logging.info(f"📥 New connection from {address}")
        sys.stdout.flush()
        
        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"\n💬 Received: {message}", flush=True)
                response = f"Server received: {message}"
                client_socket.send(response.encode('utf-8'))
                print(f"✅ Sent response for: {message}", flush=True)
                sys.stdout.flush()
        except Exception as e:
            logging.error(f"❌ Error: {e}")
            sys.stdout.flush()
        finally:
            client_socket.close()
            logging.info(f"👋 Connection closed with {address}")
            sys.stdout.flush()

if __name__ == "__main__":
    start_server()
```

#### 2.2. Client Application (client.py)
```python
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
    timestamp = datetime.now().strftime('%H:%M:%S')
    return f"[{timestamp}] {msg}"

def start_client():
    logging.info("🔌 Initializing client...")
    sys.stdout.flush()
    
    time.sleep(5)  # Wait for server to start
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
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
            message = f"Message {i+1} from client"
            logging.info(f"📤 Sending: {message}")
            client_socket.send(message.encode('utf-8'))
            
            response = client_socket.recv(1024).decode('utf-8')
            logging.info(f"📥 Received: {response}")
            
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
    ║      TCP Client Started      ║
    ╚══════════════════════════════╝
    """
    print('\033[95m' + banner + '\033[0m', flush=True)

if __name__ == "__main__":
    display_banner()
    start_client()
```

### 3. Docker Configuration Files

#### 3.1. Server Dockerfile (Dockerfile.server)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY server.py .
CMD ["python", "server.py"]
```

#### 3.2. Client Dockerfile (Dockerfile.client)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY client.py .
CMD ["python", "client.py"]
```

#### 3.3. Docker Compose Configuration (docker-compose.yml)
```yaml
version: '3'
services:
  server:
    build:
      context: .
      dockerfile: Dockerfile.server
    networks:
      - ipc_network
    tty: true
    stdin_open: true
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  client:
    build:
      context: .
      dockerfile: Dockerfile.client
    depends_on:
      - server
    networks:
      - ipc_network
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

networks:
  ipc_network:
    driver: bridge
```

### 4. Setup and Running Instructions

1. **Create Project Directory**
```bash
mkdir docker-ipc-project
cd docker-ipc-project
```

2. **Create All Required Files**
```bash
# Create all files with the contents shown above
touch server.py client.py Dockerfile.server Dockerfile.client docker-compose.yml
```

3. **Build and Run**
```bash
# Build containers
docker-compose build

# Run both containers
docker-compose up

# Or run separately in different terminals:
docker-compose up server    # Terminal 1
docker-compose up client    # Terminal 2
```

4. **Useful Commands**
```bash
# Stop all containers
docker-compose down

# View logs
docker-compose logs server
docker-compose logs client

# Follow logs in real-time
docker-compose logs -f server
docker-compose logs -f client

# Check container status
docker-compose ps

# Remove all containers and images
docker system prune -a
```

### 5. Expected Output

#### Server Output:
```
Starting server...
12:34:56 [SERVER] 🚀 Server is running on port 5000
Waiting for new connections...
12:34:58 [SERVER] 📥 New connection from ('172.18.0.3', 49123)
💬 Received: Message 1 from client
✅ Sent response for: Message 1 from client
```

#### Client Output:
```
╔══════════════════════════════╗
║       Client Started      ║
╚══════════════════════════════╝

12:34:56 [CLIENT] 🔌 Initializing client...
12:34:56 [CLIENT] 🔍 Looking for server...
12:34:58 [CLIENT] ✨ Connected to server successfully!
12:34:58 [CLIENT] 📤 Sending: Message 1 from client
12:34:58 [CLIENT] 📥 Received: Server received: Message 1 from client
--------------------------------------------------
```

### 6. Troubleshooting

1. **If containers don't start:**
```bash
docker-compose down
docker system prune -a
docker-compose up --build
```

2. **If server isn't visible to client:**
- Check network configuration in docker-compose.yml
- Ensure server name matches in client.py ('server', 5000)

3. **If logs aren't visible:**
- Use `docker-compose logs -f` command
- Check logging configuration in docker-compose.yml

### 7. Additional Notes

- The server runs continuously until stopped
- The client sends 5 messages and then exits
- Both applications use colored output for better visibility
- Logs are stored with rotation (max 10MB, 3 files)
- Network communication is handled through Docker's bridge network

