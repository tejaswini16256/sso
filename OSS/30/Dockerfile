# Use an official GCC image
FROM gcc:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Compile the C program
RUN gcc -o linkedlist linkedlist.c

# Run the linked list program
CMD ["./linkedlist"]
