initialize_building_variables
==============================



Function
--------

.. autofunction:: flexgridpy.electrical_models.variables.def_building_var.initialize_building_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_building_var.initialize_building_flex_variables

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_building_variables

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
