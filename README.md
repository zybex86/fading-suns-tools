# fading-suns-tools
Tools for DMs of the tabletop RPG game Fading Suns

## Requirements

* Python >= 3.8
* Django == 3.2
* Docker
* Docker-compose

## Overview

This app is a universal toolkit for Dungeon Masters to manage character sheets, NPCs and most importantly battle and tests.

## Local installation

1. Clone repository from github:

        git clone https://github.com/zybex86/fading-suns-tools.git

1. Create a virtual environment:

        mkvirtualenv -p python3 fst

1. Activate the virtual environment:

        workon fst

1. Update pip:

        pip install -U pip

1. Install all dependencies:

        pip install -r requirements/requirements-all.txt

1. Install the application in edit mode:

        pip install -e .

1. Create a container with the PosqtgreSQL database:

        docker run --name fst_postgresql -p 5432:5432 -e POSTGRES_DB=fst, -e POSTGRES_USER=fst -e POSTGRES_PASSWORD=fst -d postgres:13-alpine

1. Make the initial migration:

        fst-manage.py migrate

1. Create a super user account:

        fst-manage.py createsuperuser

1. Run the development server:

        fst-manage.py runserver

The application is available under `http://127.0.0.1:8000`.
Access to the administration panel is available under `http://127.0.0.1:8000/admin`
using the credentials of the super user created using `fst-manage.py createsuperuser`

## Configuration

* Configuration files available in `fst/settings`.
* `base.py` - base app configuration.
* `devel.py` - configuration for development.
* `test.py` - configuration for tests.
* You can use your any of the above files or use your own by defining it in the
`DJANGO_SETTINGS_MODULE` env variable.

## Tests

Unit tests run using *PyTest*.
You can run them using the `pytest` command, using the dedicated scripts or by
using the `tox` command.

## Docker

To run the application in production, you need to install the `Docker` and `docker-compose`
tools on the target machine. Example instalation on Ubuntu:

        sudo curl https://releases.rancher.com/install-docker/19.03.sh | sh
        sudo apt install python-pip
        pip install -U pip docker-compose

---
