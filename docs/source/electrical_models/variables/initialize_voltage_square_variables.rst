initialize_voltage_square_variables
====================================

Function
--------

.. code-block:: python

   initialize_voltage_square_variables(manager, voltage_name_prefix=None)

**Module:** ``flexgridpy.electrical_models.variables.def_voltage_var``

.. code-block:: python

   initialize_voltage_square_stochastic_variables(manager, voltage_name_prefix=None)

**Module:** ``flexgridpy.electrical_models.variables.def_voltage_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_voltage_square_variables(...)

Description
-----------

Creates the squared voltage magnitude variable :math:`v_{i,t} = |V_{i,t}|^2` for
each bus and time step. Required for the DistFlow OPF formulation.

Bounds
------

.. math::

   v_i^\min \leq v_{i,t} \leq v_i^\max

where bounds come from ``anc_Vars.System_Data_Nodes['min_v']`` and ``['max_v']``.

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``voltage_name_prefix`` (str)
     - Registered variable name (e.g. ``"voltage"``)


See Also
--------

* :doc:`../constraints_distflow/add_voltage_power_flow_df_wos`
