# Base stage
FROM node:16.16.0 AS base
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build stage
FROM base AS build
ARG HERMES_FE_PORT
RUN npm run build

# Development stage
FROM base AS development
ARG HERMES_FE_PORT

# Expose the port for development
EXPOSE $HERMES_FE_PORT

# Start the development server
CMD ["npm", "run", "dev"]

# Production stage
FROM node:16.16.0 AS production
WORKDIR /app

# Copy the built files from the build stage
COPY --from=build /app/dist /app/dist

# Install only production dependencies
COPY package*.json ./
RUN npm install --only=production

# Expose the port for production
EXPOSE 3000

# Use a lightweight HTTP server to serve the static files
RUN npm install -g serve
CMD ["serve", "-s", "dist"]
