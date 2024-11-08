#!/bin/bash

# Set the hostname
echo "127.0.0.1 ValidateCard.local" | sudo tee -a /etc/hosts

# Run the Docker Compose deployment
docker-compose up --build -d