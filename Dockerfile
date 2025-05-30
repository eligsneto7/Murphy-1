FROM python:3.11-slim

WORKDIR /app

# Copy all files first
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Verify uvicorn installation
RUN python -c "import uvicorn; print('uvicorn successfully installed')"

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 