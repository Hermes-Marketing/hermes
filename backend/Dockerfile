# Dockerfile in backend directory

# Base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Declare the build argument (although not directly used here, it's kept for build-time context)
ARG HERMES_BE_PORT

# Copy backend files into the container
COPY . /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE ${HERMES_BE_PORT}

# Run the application using the shell form of CMD to allow variable substitution
CMD uvicorn main:app --host 0.0.0.0 --port ${HERMES_BE_PORT}
