# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the source code into the container
COPY app/ .

# Expose port 8000
EXPOSE 8000

# Set the entry point command
CMD ["python", "main.py"]
