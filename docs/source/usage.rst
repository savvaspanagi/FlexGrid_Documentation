Getting Started
===============

.. _installation:

Installation
------------

FlexGridPy requires Python 3.10+ and integrates with **Pyomo**, **pandapower**, **pandas**, and **numpy**.

Install the library from the FlexGridPy repository:

.. code-block:: console

   $ git clone <flexgridpy-repo-url>
   $ cd FlexGridPy
   $ pip install -e .

Install documentation dependencies:

.. code-block:: console

   $ cd FlexGrid_Documentation
   $ pip install -r docs/requirements.txt

Minimal Example
---------------

FlexGridPy builds a Pyomo optimization model on top of a pandapower network.
The central entry point is :doc:`manager` (:class:`~flexgridpy.electrical_models.Manager.Manager`).

.. code-block:: python

   import pandapower as pp
   from flexgridpy.electrical_models.Manager import Manager

   net = pp.networks.case33bw()
   mgr = Manager(net)

   mgr.initialize_sets()
   mgr.line_param()
   mgr.load_profile_param()
   mgr.transformer_param()
   mgr.addTime(timeframe=24, time_interval=1)

   mgr.initialize_voltage_square_variables()
   mgr.initialize_branch_square_variables()
   mgr.add_active_power_flow_df_wos_constraint()
   mgr.add_reactive_power_flow_df_wos_constraint()
   mgr.add_voltage_power_flow_df_wos_constraint()

Workflow
--------

A typical FlexGridPy optimization workflow follows these steps:

1. **Create or load** a pandapower ``net`` object.
2. **Initialize** :doc:`manager`.
3. **Register sets** with :meth:`~flexgridpy.electrical_models.Manager.Manager.initialize_sets`.
4. **Add parameters** (lines, loads, DER, EV, HP, prices, …).
5. **Define variables** (voltages, branch flows, flex assets, …).
6. **Add constraints** (DistFlow, BFM, EV SoC, building thermodynamics, …).
7. **Set objective** and **solve** with a Pyomo-compatible solver (e.g. IPOPT, Gurobi).

See :doc:`manager` and :doc:`electrical_models/index` for the full API reference.
