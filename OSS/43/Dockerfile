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
