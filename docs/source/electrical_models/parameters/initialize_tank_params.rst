initialize_tank_params
========================

Function
--------

.. code-block:: python

   initialize_tank_params(manager, min_temp_preference_prefix_name, max_temp_preference_prefix_name)

**Module:** ``flexgridpy.electrical_models.parameters.tank_param_fun``

.. code-block:: python

   tank_flexibility_params(manager, Ttank, Q_demand, Tsurr, min_thermal_preference_prefix_name, max_thermal_preference_prefix_name)

**Module:** ``flexgridpy.electrical_models.parameters.tank_param_fun``

.. code-block:: python

   dhw_profile_param(manager, dhw_profile_name_prefix)

**Module:** ``flexgridpy.electrical_models.parameters.dhw_profile_param``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_tank_params(...)

Description
-----------

Registers DHW (domestic hot water) stirred-tank parameters: initial temperature,
thermal capacity, heat loss coefficient, and comfort bounds.

Flexibility Parameters
----------------------

Use :func:`~flexgridpy.electrical_models.parameters.tank_param_fun.tank_flexibility_params`
for upward/downward thermal flexibility bounds of the tank.


See Also
--------

* :doc:`../constraints_hp_dhw/add_tank_thermodynamic_constraint`
