FROM python:3.12.3

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run command when container starts
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]