# Build stage
FROM node:16.16.0 AS build
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Development stage
FROM node:16.16.0 AS development

# Create app directory
WORKDIR /app/frontend

# Install app dependencies
COPY package*.json ./
RUN npm install

# Copy app source code
COPY . .

# Expose port and start the app
EXPOSE 8080
CMD ["npm", "run", "dev"]