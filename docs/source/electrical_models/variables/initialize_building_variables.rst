initialize_building_variables
==============================

Function
--------

.. code-block:: python

   initialize_building_variables(manager, model_type, Qhp_name_prefix, Tin_name_prefix, min_temp_preference_param, max_temp_preference_param, Te_name_prefix=None, max_thermal_power_param=None)

**Module:** ``flexgridpy.electrical_models.variables.def_building_var``

.. code-block:: python

   initialize_building_flex_variables(manager, model_type, Qhp_upward_name_prefix, Qhp_downward_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_building_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_building_variables(...)

Description
-----------

Creates indoor temperature and thermal state variables for the 3R2C building
envelope model at each HP bus and time step.

Variables Created
-----------------

* ``Tin[i, t]`` — indoor air temperature (°C)
* ``Te[i, t]`` — envelope / wall temperature (°C)
* Flexibility variables for upward/downward thermal flexibility (optional)


See Also
--------

* :doc:`../constraints_hp_dhw/add_building_thermodynamic_constraint`
* :doc:`../../building_modeling/temperature_tuning`
