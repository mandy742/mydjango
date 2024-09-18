 ## HEAD
# mydjango 
This README provides instructions on how to build and run the mydjango project with virtual environments (venv) and Docker.

## Description 
Creating a small website using django, with at least 3 pages, at least 1 data base driven.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

Python 3.0
Django (installed in your virtual environment)
Docker (if using Docker for containerization)


## Python 3.0 Django (installed in your virtual environment) Docker (if using Docker for containerization)
## Project Structure
Your project structure should look like this: L3T10 ├── Webpage/ ├── gitignore ├── Dockerfile ├── manage.py ├── requirements.txt

## Getting Started
To get a local copy up and running, follow these simple steps.
git clone <repository_url>

## Navigate to your project directory
cd <project_directory>

## Create a virtual environment
python -m venv venv

## Activate the virtual environment
source venv/bin/activate # On Windows, use: venv\Scripts\activate


## Install project dependencies:
pip install -r requirements.txt

## Apply migrations:
python manage.py migrate

## Start the Django development server:
python manage.py runserver


## Running with Docker
Build the Docker image (assuming you have a Dockerfile in your project root): docker build -t my-django-app . Run the Docker container: docker run -d -p 8000:8000 my-django-app:latest

Access your application in your web browser at http://localhost:8000


