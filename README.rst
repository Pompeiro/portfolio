Try it online:
`Link <https://pompeiro.eu.pythonanywhere.com/>`_

portfolio
=========

My django-based portfolio webapp. Contains two CRUD apps, one OpenCV + Django app and one app which draws ChartJS radar chart based on data from CRUD app.

portfolioapp
=========

CRUD to serve my projects on the website. Users are allowed only to view a list of projects or single project detail. Superuser can also add projects and update them.

tftchampions
=========

CRUD which allow for registered users to create/read/update/delete tft champions.

templatematching
=========

Send haystack image, pick needle image from list and get template matching result. Needle found in haystack image is marked with red rectangle.

charts
=========

Django app based on Teamfight Tactics Champions CRUD. You can pick up to 5 champions from CRUD app, and then render Chartjs radar plot with selected champions stats.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

:License: MIT

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy portfolio

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::
 // https://stackoverflow.com/questions/19069722/psycopg2-operationalerror-cursor-does-not-exist
    $ coverage run -m pytest --create-db
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest
