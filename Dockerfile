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

# Test app import with debug (this might reveal the issue)
RUN echo "=== Testing app import with debug ===" && \
    python -c "
import sys
print('Python path:', sys.path)
print('Starting app import...')
try:
    from app.main import app
    print('✅ App imports successfully')
except Exception as e:
    print('❌ App import failed:', str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)
"

EXPOSE 8000

# Add startup script with better error handling
RUN echo '#!/bin/bash\n\
echo "=== MURPHY-1 STARTUP DEBUG ==="\n\
echo "PORT: ${PORT:-8000}"\n\
echo "Starting uvicorn with extended timeout..."\n\
exec python -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level info --timeout-keep-alive 300\n\
' > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"] 