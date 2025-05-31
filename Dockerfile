FROM python:3.11-slim

WORKDIR /app

# Copy everything
COPY . .

# Debug: Verify requirements.txt is now present
RUN echo "=== Files in /app ===" && ls -la && echo "=== Checking requirements.txt ===" && cat requirements.txt

# Install dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Verify key packages
RUN python -c "import uvicorn, fastapi; print('✅ Core packages installed')"

# Test app import with debug (fixed syntax)
RUN echo "=== Testing app import with debug ===" && python -c "import sys; print('Python path:', sys.path); print('Starting app import...'); from app.main import app; print('✅ App imports successfully')"

# Make startup script executable
RUN chmod +x start_server.py

EXPOSE 8000

# Use Python script to handle PORT variable correctly
CMD ["python", "start_server.py"] 