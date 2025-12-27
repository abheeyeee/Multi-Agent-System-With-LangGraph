# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Environment variable for Ollama (default to localhost, override in compose)
ENV OLLAMA_BASE_URL=http://localhost:11434

# Run main.py when the container launches
CMD ["python", "main.py"]
