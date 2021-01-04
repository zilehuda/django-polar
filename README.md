# Django-Polar

A dockerized boilerplate for Django Rest Framework.

## Features
- DEV, STAGE and PROD docker-compose files.
- API documentation by Swagger Doc.
- API Versioning

## Todo
- Custom user model
- Authentication by Djoser

## File Structure

This repository contains the docker configuations and a django APIs.

- `docker/` contains docker-compose and nginx, uwsgi configurations

- `src/` Contains Django source files

## Development Dependencies

Django-polar requires the following to start development

- docker `(Docker version 19.03.4-ce)`

- docker-compose `(docker-compose version 1.24.1)`

## Dive into development

- Clone this repo and install the above mentioned dependencies

```sh

$ cd django-polar/docker/compose/dev/

$ docker-compose build

$ docker-compose up

```

- Open a new terminal window

```sh

$ cd beryllium/docker/compose/dev/

$ docker-compose run --rm api python manage.py migrate

$ docker-compose run --rm api python manage.py createsuperuser

```

- Open browser and visit `http://localhost/admin`

- API Documentation available at `http://localhost/docs/`


## Contact
- Zilehuda - [LinkedIn/zilehuda](https://www.linkedin.com/in/zilehuda/)