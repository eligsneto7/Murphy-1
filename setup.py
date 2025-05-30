#!/usr/bin/env python
"""Setup script for Murphy-1 application."""

from setuptools import setup, find_packages

# Read requirements from file
def read_requirements():
    """Read requirements from requirements.txt file."""
    requirements = [
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0", 
        "python-multipart>=0.0.6",
        "jinja2>=3.1.0",
        "aiofiles>=23.0.0",
        "skyfield>=1.47",
        "pytz>=2023.3",
        "requests>=2.31.0",
        "geopy>=2.4.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "astropy>=5.3.0",
        "scipy>=1.11.0"
    ]
    return requirements

setup(
    name="murphy-1",
    version="1.0.0",
    description="Interstellar-inspired astrology application with TARS companion",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "murphy-1=app.main:app",
        ],
    },
) 