# Use the official Python image from the Docker Hub
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy project
COPY . /app

# Run the Django development server
CMD ["python", "candidate.py",]