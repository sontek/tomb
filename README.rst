Intro
=================================
A set of foundational conventions to help get anyone up and running
with the Pyramid web framework.

Batteries Included
----------------------------------
- tomb_auth for configurable user authentication
- tomb_assets for asset pipeline
- tomb_cache for caching
- Pre-made templates for error pages
- Mako for templating
- Alembic for schema migrations
- Procfile for deploying to a PaaS (e.g Heroku)
- pytest for testing
- rest_toolkit
- YAML Configuration

Style (Front-end batteries!)
---------------------------------
Templating defaults are setup to use:

- http://jquery.com/
- http://modernizr.com/
- http://foundation.zurb.com/
- http://typeplate.com/
- http://fontawesome.io/

Getting Started
=================================
As an intro to tomb we'll create a simple blog application:


.. code-block:: python

    tomb new blog

This will generate a new folder `blog` with the following folders in it:

+-------------------+--------------------------------------------------------+
|  Name             |               description                              |
+===================+========================================================+
| app/              |   Contains the controllers, models, views, helpers,    |
|                   |   mailers, and assets for the application.             |
+-------------------+--------------------------------------------------------+
| scripts/          |   Tomb scripts for starting your application and any   |
|                   |   scripts you use to deploy or run your application.   |
+-------------------+--------------------------------------------------------+
| config/           |  Configure your application's routes, database, and    |
|                   |  more.                                                 |
+-------------------+--------------------------------------------------------+
| db/               |  Contains database schema and migration scripts        |
+-------------------+--------------------------------------------------------+
| lib/              | Any code that doesn't fit in controllers, models,      |
|                   | helpers, and isn't domain specific.                    |
+-------------------+--------------------------------------------------------+
| requirements.txt  |  The dependencies needed for your tomb application     |
+-------------------+--------------------------------------------------------+
| tests/            |  Unit tests and fixtures                               |
+-------------------+--------------------------------------------------------+
