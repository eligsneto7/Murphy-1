#!/usr/bin/env python3
"""Murphy-1 Startup Script for Railway"""

import os
import sys
import subprocess

def main():
    # Get PORT from environment, default to 8000
    port = os.environ.get('PORT', '8000')
    
    print(f"=== MURPHY-1 STARTUP ===")
    print(f"PORT detected: {port}")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python path: {sys.path}")
    
    # Check if app directory exists
    if os.path.exists('app'):
        print("✅ App directory found")
        print(f"   Contents: {os.listdir('app')}")
        if os.path.exists('app/templates'):
            print("✅ Templates directory found")
            print(f"   Templates: {os.listdir('app/templates')}")
        else:
            print("❌ Templates directory NOT found")
    else:
        print("❌ App directory NOT found")
    
    print(f"Starting uvicorn on port {port}...")
    
    # Start uvicorn with proper port
    cmd = [
        sys.executable, '-m', 'uvicorn', 
        'app.main:app', 
        '--host', '0.0.0.0', 
        '--port', str(port),
        '--log-level', 'info'
    ]
    
    print(f"Command: {' '.join(cmd)}")
    
    # Execute uvicorn
    os.execvp(sys.executable, cmd)

if __name__ == "__main__":
    main() 