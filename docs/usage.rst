Usage
*****

All steps required to create or update the projects conda environment are
run automatically running ``cenv`` inside the project folder:


.. attention::
    If you use cenv, each environment should only be created, updated and
    modified using `cenv`!
    This means the commands `conda install`, `conda remove` are not used
    anymore.
    Changes of the dependencies of the environment are defined inside the
    `meta.yaml` and are applied by using `cenv`.

    This means:

    * new dependency required => add it in `meta.yaml` and run `cenv`.
    * dependency not needed anymore => remove it from `meta.yaml` and run
      `cenv`.
    * need of another version of dependency => change the version of dependency
      in `meta.yaml` and run `cenv`.


Project structure
=================

A project using cenv needs at minimum the following folder structure:

.. code:: bash

    <PROJECT>
     ├── conda-build
     │   └── meta.yaml
     ├── <SOURCE_CODE>
     ├── README.md
     └── setup.py


meta.yaml
=========

The required information about the projects conda environment are extracted
from the meta.yaml.
This meta.yaml should be located inside the project folder at
``./conda-build/meta.yaml``.

The project-configuration is defined in the ``extra`` section of the
``meta.yaml``.
There you can define the name of the projects conda-environment at
``extra:env_name``.
The python version has to be defined here at ``extra:python``, too.
Also you can define requirements only needed during development but not to be
included into the resulting conda package.
These requirements have to be defined in the
``extra:dev_requirements``-section.

All other parts of the ``meta.yaml`` have to be defined as default.

A meta.yaml valid for cenv should look like the following:

.. code:: yaml+jinja

    {% set data = load_setup_py_data() %}

    package:
        name: "example_package"
        version: {{ data.get("version") }}

    source:
        path: ..

    build:
        build: {{ environ.get('GIT_DESCRIBE_NUMBER', 0) }}
        preserve_egg_dir: True
        script: python -m pip install --no-deps --ignore-installed .

    requirements:
        build:
          - python 3.6.8
          - pip
          - setuptools
        run:
          - python 3.6.8
          - attrs >=18.2,<19
          - jinja2 >=2.10
          - six >=1.12.0
          - yaml >=0.1.7

    test:
        imports:
            - example_package

    extra:
        env_name: example
        python: 3.6
        dev_requirements:
            - ipython >=7


.. attention::
    In the ``requirements:run``-section the minimal version of each package
    has to be defined like the following:

    .. code:: yaml

        - package >=0.1

    The same is required for the ``extra:dev_requirements``-section.
    Not defining a version will not create or update a conda-environment,
    because this is not the purpose of the conda-usage.
    The validity of the ``meta.yaml`` is checked in ``cenv`` using the
    `marshmallow` package.
    You can additionally add upper limits for the version like the following:

    .. code:: yaml

        - package >=0.1,<0.3

If cenv is run the environment is created / updated from the definition inside
this ``meta.yaml``.
The creation of the backup of the previous environment ensures to undo changes
if any error occurs during recreation of the environment.


.. attention::
    ``cenv`` can only update the environment if it is not activated.
    So ensure the environment to be deactivated before running ``cenv``.

Per default exporting the conda environment definition into an environment.yml
is turned off.
If you want to turn this functionality on you need to modify your
``~/.config/cenv.yml`` as described in `configuration <configuration.html>`_.


Running cenv
============

Example for the output of the ``cenv`` command:

On create:

.. code:: bash

    Creating cenv_dev
       ├── Create environment
       │   └── Created
       ├── write md5sum of meta.yaml
       │   └── updated
       └── Done

On update:

.. code:: bash

    Updating cenv_dev
       ├── Create backup
       │   └── Created
       ├── Remove existing env
       │   └── Removed
       ├── Create environment
       │   ├── Clear backup
       │   │   └── Cleared
       │   └── Created
       ├── write md5sum of meta.yaml
       │   └── updated
       └── Done
