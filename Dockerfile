FROM python:3.11-slim

WORKDIR /app

# Copy everything first
COPY . .

# Debug: List all files to verify requirements.txt is present
RUN echo "=== DEBUG: Files in /app ===" && ls -la

# Debug: Check if requirements.txt exists and show its content
RUN echo "=== DEBUG: Checking requirements.txt ===" && \
    if [ -f "requirements.txt" ]; then \
        echo "requirements.txt found! Content:"; \
        cat requirements.txt; \
    else \
        echo "requirements.txt NOT found!"; \
        echo "Files in current directory:"; \
        ls -la; \
        exit 1; \
    fi

# Upgrade pip first
RUN python -m pip install --upgrade pip

# Install requirements with verbose output
RUN echo "=== Installing requirements ===" && \
    python -m pip install -r requirements.txt --verbose

# Verify uvicorn is installed
RUN python -c "import uvicorn; print('✅ uvicorn successfully installed')"

# Verify FastAPI is installed  
RUN python -c "import fastapi; print('✅ FastAPI successfully installed')"

# Test if app can be imported
RUN python -c "from app.main import app; print('✅ App successfully imported')"

# Expose port
EXPOSE 8000

# Use explicit python path
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 