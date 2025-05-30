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
RUN python -c "from app.main import app; print('✅ App imports successfully')"

EXPOSE 8000

# Use Railway's PORT environment variable or default to 8000
CMD python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level info 