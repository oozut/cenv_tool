Configuration
*************

`cenv` uses the path `/opt/conda` as default conda-installation-folder
and `/shared/conda/envs` as default conda-environments-folder.

You can overwrite these settings with a `cenv.yml` at
`~/.config/cenv/cenv.yml` with the following content:

.. code:: yaml

    conda_folder: /opt/conda
    env_folder: /shared/conda/envs
    export_environment_yml: false

There you can define your own conda-installation-path and the
conda-environments-folder.
The functionality to export the created / updated environment into
a `environment.yml` can be activated / deactivated here, too.
Per default it is deactivated.
If this is activated, the environment.yml will be placed at
`conda-build/environment.yml`.
