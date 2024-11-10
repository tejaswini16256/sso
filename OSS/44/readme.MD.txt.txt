---

Flask Hello World Application Setup

Step 1: Create a Project Directory

1. Open a terminal and create a new directory for the Flask application:
   mkdir flask-hello-world
   cd flask-hello-world

Step 2: Set up a Virtual Environment (Optional)

1. To create a virtual environment (recommended for development):
   python3 -m venv venv
2. Activate the virtual environment:
   - On Linux: source venv/bin/activate
   - On Windows: venv\Scripts\activate

Step 3: Install Flask

1. Install Flask with pip:
   pip install flask

Step 4: Create the Flask App

1. In the project directory, create a new file named app.py with the following code:

   # app.py
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return "<h1>Hello, World!</h1>"

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=5000)

Step 5: Create the Dockerfile

1. In the project directory, create a file named Dockerfile with the following content:

   # Dockerfile
   # Use an official Python runtime as the base image
   FROM python:3.8-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install Flask in the container
   RUN pip install flask

   # Expose the port on which the Flask app will run
   EXPOSE 5000

   # Define the command to run the app
   CMD ["python", "app.py"]

Step 6: Build the Docker Image

1. Run the following command in your project directory to build the Docker image:
   docker build -t flask-hello-world .

Step 7: Run the Docker Container

1. Start a container from the newly created image with the following command:
   docker run -d -p 5000:5000 --name flask-container flask-hello-world

   -p 5000:5000 maps port 5000 on your host machine to port 5000 on the container.
   -d runs the container in detached mode.
   --name flask-container assigns a name to the container.

Step 8: Verify the Application

1. Open a web browser and go to http://localhost:5000.
2. You should see the message: Hello, World!

Step 9: Stopping the Container

1. To stop the running container:
   - Find the container ID by running:
     docker ps
   - Then stop it with:
     docker stop <container_id>






---






---

Step 1: Run Multiple Flask Containers

# Start two or more instances of your Flask app container with different container names
docker run -d --name flask-app-1 -p 5001:5000 flask-hello-world
docker run -d --name flask-app-2 -p 5002:5000 flask-hello-world

Explanation:
- flask-app-1 and flask-app-2 are names for each container instance.
- -p 5001:5000 maps port 5001 on the host to port 5000 in flask-app-1,
  and 5002 does the same for flask-app-2.

# Verify the Containers are Running
docker ps

---

Step 2: Create an NGINX Configuration File for Load Balancing

# Create an NGINX Configuration File
# Create a file named nginx.conf in a directory (e.g., in the project directory where you have the Flask app).

nginx.conf:
events {}

http {
    upstream flask_app {
        server flask-app-1:5000;
        server flask-app-2:5000;
    }
    
    server {
        listen 80;
        
        location / {
            proxy_pass http://flask_app;
        }
    }
}

Explanation:
- upstream flask_app defines a load balancing group named flask_app with two
  backend servers (flask-app-1 and flask-app-2).
- proxy_pass will forward requests from NGINX to this upstream group.

---

Step 3: Run the NGINX Container with Load Balancing

# Run the NGINX Container with the custom configuration file.

On Linux:
docker run -d --name nginx-loadbalancer -p 8080:80 --link flask-app-1 --link flask-app-2 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro nginx

On Windows:
docker run -d --name nginx-loadbalancer -p 8080:80 --link flask-app-1 --link flask-app-2 -v ${PWD}/nginx.conf:/etc/nginx/nginx.conf:ro nginx

Explanation:
- -p 8080:80 maps port 8080 on the host to port 80 in the NGINX container.
- --link flask-app-1 and --link flask-app-2 link the NGINX container to the two Flask
  app containers for network communication.
- -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro mounts the custom nginx.conf configuration file in the NGINX container as read-only.

---

Step 4: Verify Load Balancing

# Access the Load Balancer
- Open a browser and go to http://localhost:8080.
- You should see the "Hello, World!" response from the Flask app, with NGINX balancing
  requests between flask-app-1 and flask-app-2.
- If you refresh the page several times, the responses should alternate between the two Flask
  instances, as NGINX distributes the load.

# Verify Load Balancing with Commands

On Linux:
for i in {1..10}; do curl -s http://localhost:8080; echo; done

On Windows (in PowerShell):
for ($i=0; $i -lt 1000; $i++) {curl http://localhost:8080 | Out-Null}

# Verify the load balancing using docker stats:
docker stats flask-app-1 flask-app-2

---

