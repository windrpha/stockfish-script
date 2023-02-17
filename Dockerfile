FROM python:3.9

# Install any necessary dependencies
RUN pip install python-chess \
    docker

# Copy the Python script into the Docker image
COPY stockfish_script.py /app/

# Set the working directory to the app directory
WORKDIR /app

# Run the Python script when the container starts
CMD ["python", "stockfish_script.py"]