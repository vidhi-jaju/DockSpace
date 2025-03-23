# Use Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY api_gateway.py /app

# Install dependencies
RUN pip install flask requests

# Run the API Gateway
CMD ["python", "api_gateway.py"]
