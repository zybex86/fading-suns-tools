# The repo was moved
## As of today, the repo will be private and the app will be officially patroned by Ulisses Spiele International

# Fading Suns Toolkit
Tools for DMs of the tabletop RPG game Fading Suns

## Copyright Desclaimer

`Fading Suns` was created by Bill Bridges and Andrew Greenberg is a trademark and
copyright of Holistic Design Inc.

The app is delivered as is - with no added content or pre-loaded data.
If you own a copy of the `Fading Suns` rule book, you can only
provide data for personal use.

I will never add any parts of the rule book to the official repository.

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

        docker run --name fst_postgresql -p 5432:5432 -e POSTGRES_DB=fst -e POSTGRES_USER=fst -e POSTGRES_PASSWORD=fst -d postgres:13-alpine

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

All tests are placed inside their respective app folder inside the `tests` directory.
Unit tests run using *PyTest*. You can run them using the `pytest` command, using the
dedicated scripts or by using the `tox` command.

## Docker

To run the application in production, you need to install the `Docker` and `docker-compose`
tools on the target machine. Example instalation on Ubuntu:

        sudo curl https://releases.rancher.com/install-docker/19.03.sh | sh
        sudo apt install python-pip
        pip install -U pip docker-compose

---

# Contribution Guidelines

If you found a bug, please ensure that you described exactly how the bug occured,
so that the developers know how to recreate it.

If you want to propose a new feature or improvement, please write a new issue
describing the feature.

## For Developers

There are two main branches:
* `master` - the branch with the current official version of the app.
* `devel` - the branch where all new features should be merged and tested before
merging with `master`

All pull requests should target the `devel` branch.

Before starting work on an issue, make sure no one else is working on it at the moment.
Ask the Maintainers if you can take the issue. We ussually respond within 24 hours.

Fork the repository and create a new branch with the name of the issue you are
working on. Try to name the branch according to the issue you are working on
based on this example: `feature/bug-issue_number-short-description` (i.e.
`feature-1-character-model`).

Upon creating a new pull request, make sure you have added tests and you
checked your code using `flake8`.

After Code Review, your Pull Request will be either merged or rejected.
If rejected, you will be informed why the request was closed.

---
