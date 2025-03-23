# Use Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY backend.py /app

# Install Flask
RUN pip install flask

# Run the backend service
CMD ["python", "backend.py"]
