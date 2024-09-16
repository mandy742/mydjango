# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install virtualenv and create a virtual environment
RUN pip install --no-cache-dir virtualenv
RUN virtualenv venv
ENV PATH="/app/venv/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project into the container
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
