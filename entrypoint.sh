#!/bin/bash
echo "Running entrypoint.sh"

# Inicializa o servidor usando Gunicorn
exec gunicorn -w 4 -b 0.0.0.0:8080 "app.main:api_rest" --reload
