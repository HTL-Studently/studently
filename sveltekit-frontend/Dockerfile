# Use the official Ubuntu image as the base image
FROM ubuntu:latest

# Set environment variables to suppress interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update
RUN apt-get install -y curl 
RUN apt-get install git 


# Install NVM (Node Version Manager)
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Load NVM and install the latest version of Node.js
RUN export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    nvm install node && \
    nvm alias default node

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy the rest of the application files to the container
COPY . .

# Build SvelteKit app
RUN npm run build

# Expose the port that the app is running on
EXPOSE 3000

# Command to start the application
CMD ["npm", "run", "dev", "--", "--open"]
