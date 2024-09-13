# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the Django project into the container
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000
 
# Define the command to run when the container starts
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]