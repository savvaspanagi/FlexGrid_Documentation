initialize_hp_variables
=======================

Function
--------

.. code-block:: python

   initialize_hp_variables(manager, p_name_prefix, q_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_hp_var``

.. code-block:: python

   initialize_gamma_valve_variable(manager, set, gamma_valve_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_hp_var``

.. code-block:: python

   initialize_hp_flex_variables(manager, p_upward_name_prefix, p_downward_name_prefix, q_upward_name_prefix, q_downward_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_hp_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_hp_variables(...)

Description
-----------

Creates heat-pump thermal and electrical power variables, plus the gamma valve
variable that selects between space heating and DHW modes.

Variables Created
-----------------

* ``Qhp[i, t]`` — thermal power output (kW)
* ``php[i, t]`` — electrical power consumption (p.u.)
* ``gamma_valve[i, t]`` — mode selector (0 = SH, 1 = DHW)


See Also
--------

* :doc:`../constraints_hp_dhw/add_HP_operation_constraint`
