FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (if needed later you can extend this list)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml /app/pyproject.toml
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir google-adk fastapi "uvicorn[standard]"

# Copy application code
COPY . /app

# Cloud Run will provide PORT; default to 8080 for local runs
ENV PORT=8080

# Start the FastAPI app with uvicorn
CMD exec uvicorn main:app --host 0.0.0.0 --port ${PORT}



