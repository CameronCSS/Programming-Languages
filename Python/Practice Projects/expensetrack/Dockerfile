# Use Python slim image
FROM python:3.10-slim

# Prevent Python from buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure pip installs scripts are in PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy project
COPY . .

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
