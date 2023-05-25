#!/bin/sh

echo "Starting Server"

gunicorn -b 0.0.0.0:5000 app:app