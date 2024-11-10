# Base image
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the app
COPY src ./src

# Expose the application port
EXPOSE 3000

# Set default directory for serving files
ENV HOST_DIR=/mounted

# Run the app
CMD ["node", "src/server.js"]
