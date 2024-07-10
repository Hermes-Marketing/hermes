# Getting Started

# Accessing FastApi Documentation

Useful for testing apis

http://localhost:8000/docs

# Test db connection

`set ENV=dev` or `set ENV=prod`

`python firebase_config.py`

for dev and prod you should expect to get data from the db back indicating what env the data resides in

# backend structure

app/
|-- api/ # Contains routes for handling HTTP requests
| |-- routes/ # Defines the endpoints for your application
|-- core/ # Core functionalities and services used across the application
|-- database/ # Database connection
|-- models/ # Database models (ORM) defining the structure of your data
|-- schemas/ # Data validation schemas
|-- tests/ # Test cases for the application
|-- utils/ # Utility functions and helpers
