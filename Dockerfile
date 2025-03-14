# Image base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Set environment variable
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
