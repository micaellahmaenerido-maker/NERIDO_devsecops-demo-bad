# Security Flaw 1: Using an outdated, vulnerable base image (Debian Buster)
FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install vulnerable dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

EXPOSE 5000

# Security Flaw 2: Running as root (no user context switch)
# Security Flaw 3: Running the built-in Flask dev server in production
CMD ["python", "app/main.py"]