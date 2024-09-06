# Django Application

## Setup

### Virtual Environment
1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Install project dependencies:
pip install -r requirements.txt

## Apply migrations:
python manage.py migrate

## Start the Django development server:
python manage.py runserver
Access your application in your web browser at http://localhost:8000

## Running with Docker
Build the Docker image (assuming you have a Dockerfile in your project root):
docker build -t my-django-app .
Run the Docker container:
docker run -d -p 8000:8000 my-django-app
Access your application in your web browser at http://localhost:8000.
If your application requires environment variables, create a .env file 

