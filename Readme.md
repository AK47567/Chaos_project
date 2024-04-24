# Chaos Project

Welcome to the Chaos Project! This project is aimed at generating images based on user-defined prompts using Celery and Django.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before running the project, ensure you have the following installed:

- Python (version 3.6 or higher)
- Redis (as the message broker for Celery)
- Django (Python web framework)
- Celery (Distributed Task Queue)

### Installing

1. Clone the repository(change branch to master, dont use main default) to your local machine:

   ```bash
   git clone https://github.com/AK47567/Chaos_project.git

2. cd chaos_project

3.Create a Virtual Environment

    python -m venv venv

4. Activate the virtual environment 

    venv\scripts\activate

5.Install all the required dependencies

    pip install -r requirements.txt

6. Start the Celery worker

    celery_config -A chaos_project worker -l INFO

7. Run the server 

    python manage.py runserver

8. Now based on the prompt that is given by the user, it will generate the image and store it in a image file in the same directory.

    
