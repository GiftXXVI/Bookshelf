# Project Documentation
## Bookshelf
Bookshelf is a web-based service for managing books. It allows users to create, update, delete, search and retrieve book records. It also contains an API which allows integration with other systems and enables development of apps for desktop and mobile clients.

The motivation behind bookshelf is to enable easy management, searching and retrieval of book information and replace manual paper based indexing systems. It is also the best option for managing a purely online library for Online Learning Institutions.

The Bookshelf API is written in Python and follows the PEP8 Guidelines *https://www.python.org/dev/peps/pep-0008/*

## Getting Started
### Dependencies
Before you can run the application, you need to have the following dependencies in place:
```bash
pip install aniso8601
pip install click
pip install Flask
pip install Flask-Cors
pip install Flask-RESTful
pip install Flask-SQLAlchemy
pip install itsdangerous
pip install Jinja2
pip install MarkupSafe
pip install psycopg2-binary
pip install pytz
pip install six
pip install SQLAlchemy
pip install Werkzeug
```

### Installation
To start the web API; make sure that the database is running, navigate to the backend directory and run the following commands:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
If the database is not running, it can be started using the following command:
```bash
sudo service postgresql start
```

You can then verify that the API is accessible by running the following curl command:

```bash
curl http://127.0.0.1:5000/books
```

### Unit Tests
Unit tests have been defined inside the file backend/test_flaskr.py

You should run the tests using the following command to verify that everything has been installed correctly:

```bash
python3 test_flaskr.py
```

## API Reference
The API Reference is defined in the file backend/README.md

## Deployment
Currently, there is no live environment as this is a est project. However, changes can be submitted to the GitHub repository.

## Authors

The code comes from a Udacity course, but most of it has been modified by Gift Chimphonda during the course of studies.

## Acknowledgements

StackOverflow was immensely helpful on a few occasions.