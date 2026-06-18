initialize_hp_variables
=======================

Description
-----------

Creates heat-pump thermal and electrical power variables, plus the gamma valve
variable that selects between space heating and DHW modes.

Variables Created
-----------------

* ``Qhp[i, t]`` — thermal power output (kW)
* ``php[i, t]`` — electrical power consumption (p.u.)
* ``gamma_valve[i, t]`` — mode selector (0 = SH, 1 = DHW)

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_hp_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_gamma_valve_variable

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_hp_flex_variables

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_hp_variables

See Also
--------

* :doc:`../constraints_hp_dhw/add_HP_operation_constraint`
