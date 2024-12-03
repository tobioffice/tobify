#!/bin/bash
echo "Installing dependencies..."
pip3 install -r requirements.txt

echo "Running migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collecting static files..."
rm -rf staticfiles
mkdir -p staticfiles
python3 manage.py collectstatic --noinput