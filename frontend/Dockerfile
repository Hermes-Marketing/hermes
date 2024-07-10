# Build stage
FROM node:16.16.0 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Development stage
FROM node:16.16.0 AS development

# Set working directory
WORKDIR /app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Copy app source code
COPY . .

# Fix permissions
RUN chown -R node:node /app/node_modules

# Use non-root user
USER node

# Expose port and start the app
EXPOSE 8080
CMD ["npm", "run", "dev"]