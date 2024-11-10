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
