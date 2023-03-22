# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the app
CMD gunicorn travelrecs.wsgi:application --bind 0.0.0.0:8080 --workers 3
