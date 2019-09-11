cenv
****

.. image:: _static/coverage.svg

.. image:: https://badge.fury.io/py/cenv-tool.svg
   :target: https://pypi.python.org/pypi/cenv-tool/

.. image:: https://img.shields.io/pypi/pyversions/cenv-tool.svg
   :target: https://pypi.python.org/pypi/cenv-tool/

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

.. image:: https://readthedocs.org/projects/cenv-tool/badge/?version=latest
   :target: https://cenv-tool.readthedocs.io/en/latest/?badge=latest


Tool to create / update conda environments from ``meta.yaml``.

Due to the redundant dependency information inside the ``meta.yaml`` (required
to create the conda-package) and the ``environment.yml`` (as definition file
for the conda-environment during development and for production), ``cenv``
(short form for ``conda-env-manager``) was created to make the ``meta.yaml``
the only relevant file and to create and update conda-environment from the
definition inside this ``meta.yaml``.
The name of the conda-environment to create / update is defined in the section
``extra`` and the variable ``env_name`` inside the ``meta.yaml`` (at
``conda-build/meta.yaml``).

The steps run by cenv:


    * creation of a backup if the environment already exists followed by the
      removal of the previous environment.
    * creation of the environment as defined in the ``meta.yaml``.
      If any failures occurred during creation and the backup was created, the
      command to reset the backup-version can be used.
    * if enabled in the config file the environment.yml is exported after
      creation / update of the environment.



The usage of cenv reduces the conda commands to use to the following:

    * ``conda activate ...`` to activate the environment
    * ``conda deactivate`` to deactivate an environment
    * ``conda info`` to show information about the currently activated
      environment
    * ``conda search ...`` to search for availability of a package in the conda
      channels.
    * ``conda remove -n ... --all`` to remove an environment
    * ``cenv`` to create / update an environment


Table of contents
*****************

.. toctree::
   :maxdepth: 2

   installation.rst
   configuration.rst
   usage.rst
   modules_base.rst
   about.rst
   license.rst
   impressum.rst
