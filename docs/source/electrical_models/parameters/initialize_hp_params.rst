initialize_hp_params
====================

Function
--------

.. code-block:: python

   initialize_hp_params(manager, Tout_param, COP_prefix_name, min_thermal_power_prefix_name, max_thermal_power_prefix_name, min_temp_preference_prefix_name, max_temp_preference_prefix_name)

**Module:** ``flexgridpy.electrical_models.parameters.hp_param_fun``

.. code-block:: python

   hp_flexibility_params(manager, Tin, Te, Tout, Qsol, min_temp_flexibility_prefix_name, max_temp_flexibility_prefix_name, min_thermal_flexibility_prefix_name, max_thermal_flexibility_prefix_name)

**Module:** ``flexgridpy.electrical_models.parameters.hp_param_fun``

.. code-block:: python

   initialize_hp_stochastic_params(manager, hp_scenario_dict, Tout_param, COP_prefix_name, min_thermal_power_prefix_name, max_thermal_power_prefix_name, min_temp_preference_prefix_name, max_temp_preference_prefix_name)

**Module:** ``flexgridpy.electrical_models.parameters.hp_param_fun``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_hp_params(...)

Description
-----------

Registers heat-pump COP curves, thermal power limits, and building thermal
parameters for each bus in ``SHPbuses``.

Parameters Registered
---------------------

Includes COP coefficients, minimum/maximum thermal power, and building RC
parameters (resistances and capacitances) used in the 3R2C thermodynamic model.

Flexibility Parameters
----------------------

Use :func:`~flexgridpy.electrical_models.parameters.hp_param_fun.hp_flexibility_params`
to additionally register upward/downward thermal flexibility bounds.


See Also
--------

* :doc:`../../building_modeling/temperature_tuning`
* :doc:`../constraints_hp_dhw/add_building_thermodynamic_constraint`
