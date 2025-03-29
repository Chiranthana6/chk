# Use correct Python image name
FROM python:3.12.3-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY HelloWorld.py /app
# Run the script inside the container
CMD ["python", "HelloWorld.py"]
