#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories if they don't exist
mkdir -p instance
mkdir -p staticfiles_build

# Set up environment variables (if needed)
# export FLASK_APP=tobify
# export FLASK_ENV=production

# Run any database migrations or initialization if needed
# flask db upgrade

# Collect static files
python manage.py collectstatic --noinput

echo "Build completed successfully!"
