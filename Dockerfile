# Use the official Python slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to install dependencies
COPY requirements.txt ./

# Copy the application code into the container
COPY app/ ./app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your Python script (overridden by docker-compose)
CMD ["python", "-m", "main.py"]
