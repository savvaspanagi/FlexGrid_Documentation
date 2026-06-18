initialize_hp_params
====================

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

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.hp_param_fun.initialize_hp_params

.. autofunction:: flexgridpy.electrical_models.parameters.hp_param_fun.hp_flexibility_params

.. autofunction:: flexgridpy.electrical_models.parameters.hp_param_fun.initialize_hp_stochastic_params

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_hp_params

.. automethod:: flexgridpy.electrical_models.Manager.Manager.hp_flexibility_params

See Also
--------

* :doc:`../../building_modeling/temperature_tuning`
* :doc:`../constraints_hp_dhw/add_building_thermodynamic_constraint`
