Installation
************

To install cenv simply run:

.. code:: bash

    pip install cenv_tool

Now run `init_cenv` to create the relevant config-files and add the
autoactivate- and autoupdate-shell-function to your `.bashrc` / `.zshrc`.


autoactivate and autoupdate
===========================

Per default these features are deactivated, even if added to your shell by
running `init_cenv`.


autoactivate-feature
--------------------

The autoactivate-feature activates the conda-environment as named
`extra`-section in the meta.yaml located at `conda-build/meta.yaml`, if the
environment exists.
To activate the autoactivate-features run:

.. code:: bash

    autoactivate_toggle


autoupdate-feature
------------------

The autoupdate checks if the content of the meta.yaml changed.
The current state is stored as a md5sum in `conda-build/meta.md5`.
If it changed the cenv-process is called.

For the autoupdate-feature run:

.. code:: bash

    autoupdate_toggle
