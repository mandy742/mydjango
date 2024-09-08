
# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Copy the Django project into the container
COPY . /app/

# Define the command to run when the container starts
CMD ["python", "candidate.py"]
=======
# Use the official Python image from the Docker Hub
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy project
COPY . /app

# Run the Django development server
CMD ["python", "candidate.py",]
>>>>>>> container
