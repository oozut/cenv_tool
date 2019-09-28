Development of cenv
===================


Develop cenv
------------

To create / update the dev environment to develop cenv run the pre-commit hooks
manually:

.. code-block:: bash

   pyenv local 3.7.3
   dephell venv shell --env=dev
   dephell deps install
   pre-commit run --all-files


Running tests
-------------

To create / update the test environment run:

.. code-block:: bash

   dephell venv shell --env=pytest
   dephell deps install


To run all tests run the following command:

.. code-block:: bash

   dephell project test --env=pytest


Updating the docs
-----------------

To create / update the docs environment run:

.. code-block:: bash

   dephell venv shell --env=docs
   dephell deps install --env=docs


To create / update the docs first run the tests as described above.
Then run:

.. code-block:: bash

   dephell venv shell --env=docs
   sphinx-apidoc -f -o docs cenv_tool && sphinx-build -W docs docs/build
