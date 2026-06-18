initialize_tank_params
========================

Description
-----------

Registers DHW (domestic hot water) stirred-tank parameters: initial temperature,
thermal capacity, heat loss coefficient, and comfort bounds.

Flexibility Parameters
----------------------

Use :func:`~flexgridpy.electrical_models.parameters.tank_param_fun.tank_flexibility_params`
for upward/downward thermal flexibility bounds of the tank.

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.tank_param_fun.initialize_tank_params

.. autofunction:: flexgridpy.electrical_models.parameters.tank_param_fun.tank_flexibility_params

.. autofunction:: flexgridpy.electrical_models.parameters.dhw_profile_param.dhw_profile_param

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_tank_params

.. automethod:: flexgridpy.electrical_models.Manager.Manager.tank_flexibility_params

See Also
--------

* :doc:`../constraints_hp_dhw/add_tank_thermodynamic_constraint`
