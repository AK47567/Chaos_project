Chaos Project
Welcome to the Chaos Project! This project is aimed at generating images based on user-defined prompts using Celery and Django.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Before running the project, ensure you have the following installed:

Python (version 3.6 or higher)
Redis (as the message broker for Celery)
Django (Python web framework)
Celery (Distributed Task Queue)
Installing
Clone the repository(change branch to master, dont use main default) to your local machine:

git clone https://github.com/AK47567/Chaos_project.git
cd chaos_project

Create a Virtual Environment

python -m venv venv
Activate the virtual environment

venv\scripts\activate

Make the necessary migrations

Add the database of your choice in settings and then run the following commands

python manage.py makemigrations
python manage.py migrate

Install all the required dependencies

pip install -r requirements.txt
Start the Celery worker

celery_config -A chaos_project worker -l INFO

Run the server

python manage.py runserver

Now based on the prompt that is given by the user, it will generate the image and store it in a image file in the same directory.

P.S. Dont forget to generate your API key and enter it in the authorization section in the views.py file.
