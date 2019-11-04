Using py-proj-cookie
=====================

Reasons to use this:
---------------------

- Simple project setup that takes advantage of using environment variables and ``Make`` as a build tool.
- Creates a virtual environment using ``Make`` and environment variables to avoid confusing ``PYTHONPATH`` issues with your system's Python.

You can customize from here to make the cookie your own to set up your projects just the way you like.

----

Open a new shell and get `cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`_ onto your system Python.

.. code:: bash

	$ git clone git@github.com:gpetepg/py-proj-cookie.git
	$ pip install cookiecutter
	$ cd <desired-project-location>
	$ cookiecutter path/to/py-proj-cookie

The previous command will prompt the values in cookiecutter.json to be filled out. Use the following format.

.. code:: bash

	    project_name: Your project name in lowercase, if you need a space is need use a `-` e.g. project-name
	    PROJECT_NAME: Your project name in uppercase, if you need a space is need use a `_` e.g. PROJECT_NAME
	    author: The author of the project
	    description: A generic description of your project

For initial setup you will need to source, make the `ve` and then source `setup.env` to activate it.

.. code:: bash
	
	$ cd <your-project>
	$ source setup.env
	$ make
	$ source ve/bin/activate

When returning to your project just source the environment file. This will source your environment variables and ve at the same time.

.. code:: bash
	
	$ source setup.env

To increase ease of use you can add this cookie to your ``~/.bash_profile``.

.. code:: bash

	alias py-proj="cookiecutter /Users/<User>/<path_to>/py-proj-cookie/"

Resources
---------------------
- GNU Make manual: https://www.gnu.org/software/make/manual/html_node/index.html
- GNU Bash manual: https://www.gnu.org/software/bash/manual/html_node/index.html
