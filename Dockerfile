FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY app.py .

# Expose the port on which the app will run (if needed)
# This depends on how RunPod sets up listening, so adjust accordingly.
# If runpod.serverless.start() listens on a particular port, expose it here.
EXPOSE 8080

# Set the command to run the application
CMD ["python", "app.py"]