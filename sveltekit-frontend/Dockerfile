# # Use the official Ubuntu image as the base image
# FROM ubuntu:latest

# # Set environment variables to suppress interactive installation
# ENV DEBIAN_FRONTEND=noninteractive

# # Install dependencies
# RUN apt-get update
# RUN apt-get install -y curl 
# # RUN apt-get install git 


# # Install NVM (Node Version Manager)
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# # Load NVM and install the latest version of Node.js
# RUN export NVM_DIR="$HOME/.nvm" && \
#     [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
#     nvm install node && \
#     nvm alias default node

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the package.json and package-lock.json files to the container
# COPY package*.json ./

# # Install dependencies
# # RUN npm install --production

# # Copy the rest of the application files to the container
# COPY . .

# # Build SvelteKit app
# RUN npm run build

# # Expose port 5173 for the app
# EXPOSE 5173

# # Define the command to run the app
# CMD ["npm", "run", "dev", "--", "--open", "--port", "5173"]


# Use an official Node runtime as a parent image
FROM ubuntu:latest

# Update package lists and install necessary dependencies
RUN apt-get update && \
    apt-get install -y curl xdg-utils && \ 
    # curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Bundle app source
COPY . .

# Build the SvelteKit app
#RUN npm run build

# Expose port 5173 for the app
EXPOSE 5173

# Define the command to run the app
CMD ["npm", "run", "dev", "--", "--open", "--port", "5173"]
