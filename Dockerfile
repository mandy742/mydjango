# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the Django project into the container
COPY . /app/

# Define the command to run when the container starts
CMD ["python", "candidate.py"]