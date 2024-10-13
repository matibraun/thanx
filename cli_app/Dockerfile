# Set the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /cli_app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    pkg-config \
    libcairo2-dev \
    cmake \
    cython3 \
    build-essential \
    libgirepository1.0-dev \
    gir1.2-gtk-3.0 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt from the root folder to the cli_app folder
COPY requirements.txt /cli_app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files
COPY . /cli_app/

# Expose any necessary ports
EXPOSE 5000
