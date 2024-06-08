# Use python:3.12-alpine base image
FROM python:3.12-alpine

# Set working directory for app
WORKDIR /app

# Upgrade pip for better practices
RUN pip install --upgrade pip

# Copy requirements.txt for installation
COPY requirements.txt .

# Install dependencies from requirements.txt (no cache)
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project directory
COPY . .

# Run app.py as the entry point
CMD ["python3", "app.py"]
