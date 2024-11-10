# Step 1: Start with Ubuntu base image
FROM ubuntu:latest

# Step 2: Install OpenJDK with retries and fix-missing option
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends openjdk-17-jdk && \
    rm -rf /var/lib/apt/lists/*

# Step 3: Create a working directory
WORKDIR /app

# Step 4: Copy your Java application (assuming Main.java is in the same directory)
COPY Main.java .

# Step 5: Compile the Java application
RUN javac Main.java

# Step 6: Set the entry point to run the Java application
CMD ["java", "Main"]
