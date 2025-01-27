# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port for the Flask app
EXPOSE 8080

# Start the Flask app with Gunicorn
CMD ["gunicorn", "-w", "3", "-k", "gevent", "-b", "0.0.0.0:8080", "--timeout", "60", "--graceful-timeout", "30", "--access-logfile", "-", "--error-logfile", "-", "--preload", "--worker-connections", "1000", "main:app"]
CMD ["python", "./main.py"]
