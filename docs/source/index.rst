Welcome to FlexGridPy's documentation!
======================================

.. image:: ../Image/FlexGrid.png
   :alt: FlexGridPy Logo
   :align: center
   :width: 300

**FlexGridPy** is a Python library for researchers and engineers
working on the intelligent operation of power systems.
It provides modular tools for:

- Modeling and solving convex and non-convex Optimal Power Flow (OPF) problems,
- Optimizing electric vehicle (EV), heat pump (HP), and distributed energy resource (DER) integration,
- Tuning grey-box thermal models for buildings (models that can be used to simulate the behavior of buildings temperature),
- Electricity market clearing (copperplate and more sophisticated by integrating electrical moodel constraints),
- Generation of probabilistic transportation data for EV studies.

FlexGridPy is designed for **flexibility-aware modeling**, combining control,
simulation, and optimization in a unified and extensible framework. However, extra constraints 
can be easily added since it is built on top of Pyomo, using the normal Pyomo syntax.

It integrates seamlessly with common open-source tools (Pyomo, NumPy, Pandas,
Matplotlib, pandapower) and supports scalable experiments.

Check out the :doc:`usage` section for installation and a minimal example.

.. note::

   This project is under active development.

Contents
--------

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   usage

.. toctree::
   :maxdepth: 1
   :caption: Manager

   manager

.. toctree::
   :maxdepth: 2
   :caption: Electrical Models

   electrical_models/index

.. toctree::
   :maxdepth: 2
   :caption: Market

   market/index

.. toctree::
   :maxdepth: 2
   :caption: Building Modeling

   building_modeling/index

.. toctree::
   :maxdepth: 2
   :caption: Transportation

   transportation/index

.. toctree::
   :maxdepth: 2
   :caption: About FlexGridPy

   About
