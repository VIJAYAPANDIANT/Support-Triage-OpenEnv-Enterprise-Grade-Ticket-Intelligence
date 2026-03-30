# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pydantic openai pyyaml

# Define environment variable
ENV OPENAI_API_KEY=""

# Run baseline.py when the container launches
CMD ["python", "scripts/baseline.py"]
