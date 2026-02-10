# Use the official Python 3.8 slim image as the base
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set environment so that SSH works correctly
ENV PYTHONUNBUFFERED=1

# Start SSH server in background and then run the Flask app
CMD python app.py