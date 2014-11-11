Getting Started
=================================
As an intro to tombo we'll create a simple blog application:


.. code-block:: python

    tomb --new blog

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
