Electrical Models
=================

FlexGridPy's electrical models build a **Pyomo optimization problem** on top of a
`pandapower <https://pandapower.readthedocs.io>`_ network. The central class is
:class:`~flexgridpy.electrical_models.Manager.Manager`, which provides a unified API
for sets, parameters, variables, and constraints.

The modeling workflow mirrors pandapower's element-based structure, but each
component is registered as a Pyomo set, parameter, variable, or constraint group.

.. toctree::
   :maxdepth: 2
   :caption: Electrical Models

   electrical_models/manager
   electrical_models/sets
   electrical_models/parameters
   electrical_models/variables
   electrical_models/constraints_distflow
   electrical_models/constraints_bfm
   electrical_models/constraints_ac_pf
   electrical_models/constraints_flow
   electrical_models/constraints_ev
   electrical_models/constraints_hp_dhw
   electrical_models/constraints_stochastic
   electrical_models/power_flow
   electrical_models/initializations

Quick Links
-----------

* :doc:`electrical_models/manager` — Main orchestrator class
* :doc:`electrical_models/sets` — Network and time sets
* :doc:`electrical_models/parameters` — Line, load, DER, EV, HP parameters
* :doc:`electrical_models/variables` — Voltage, branch, DER, EV variables
* :doc:`electrical_models/constraints_distflow` — DistFlow OPF (without shunt)
* :doc:`electrical_models/constraints_bfm` — Branch Flow Model
* :doc:`electrical_models/constraints_ev` — EV SoC and flexibility
* :doc:`electrical_models/power_flow` — PF vs OPF comparison utilities
