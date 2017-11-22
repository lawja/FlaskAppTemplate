# Flask App Template
A repo for a template flask app that runs a Flask Development Server or Gunicorn

Assuming dependencies are installed, it can be run with `python manage.py runserver`
This will make it available at localhost:1337

## Table of Contents
1. [Installation](#installation)
2. [Setting up your Flask App](#Setting-up-your-Flask-App)
3. [Database Configuration](#Database-Configuration)
4. [Runing you App with Gunicorn](#Running-your-App-with-Gunicorn)


## Installation
To install this Flask app template simply clone this repository with

`git clone https://github.com/lawja/FlaskAppTemplate.git`

You could also download this repository as a .zip folder
## Setting up your Flask App
To set up your flask app you'll want to do two things; run `setup.py`, and change `config.py` accordingly.

Running `setup.py` simply installs the dependencies of the Flask App Template. Before doing this I suggest creating a virtual environment. To create a virtual environment run
```
virtualenv venv
./venv/bin/activate
```
This creates a virtual environment which in turn installs the project dependencies locally to the virtual environment and not to the global python package index.

Now, run `setup.py` with

`python3 setup.py`

This installs the dependencies stored in `requirements.txt`
Seconndly, edit `config.py` accordingly. In `config.py` you can change the author name, version number, and other stuff such as database credentials (which will be important to application functionality).
## Database Configuration
Currently I only have MongoDB with PyMongo working for the database of this flask app, mainly because I like it the most.
To edit the database credentials, simply edit `DB_USER` and `DB_PATH` in `config.py` and edit the DB URI in `manage.py`
## Running your App with Gunicorn
Because the Flask development server limits performance and isn't well suited for a production environment, one may want to use gunicorn.

To run the app with gunicorn use

`python manage.py gunicorn`

If you find any issues create an issue or a pull request to fix the issue
