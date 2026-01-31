# Base image : python + linux (pulling from Docker Hub)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY hangman.py .

# Run the game
CMD ["python", "hangman.py"]
