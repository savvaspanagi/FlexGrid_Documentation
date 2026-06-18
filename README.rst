FlexGridPy Documentation
======================

Documentation for the FlexGridPy library, built with Sphinx and hosted on Read the Docs.

Build locally
-------------

.. code-block:: console

   pip install -r docs/requirements.txt
   cd docs
   make html

The HTML output is in ``docs/build/html/``.

Structure
---------

* **Electrical Models** — Manager API, sets, parameters, variables, OPF constraints
* **Market** — Copperplate and DC-OPF market clearing
* **Building Modeling** — RC model tuning and simulation
* **Transportation** — Probabilistic EV data generation

Requirements
------------

FlexGridPy must be available on the Python path. For local builds, place the
``FlexGridPy`` repository as a sibling directory to ``FlexGrid_Documentation``.
