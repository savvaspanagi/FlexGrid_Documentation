initialize_tank_variables
=========================

Function
--------

.. code-block:: python

   initialize_tank_variables(manager, model_type, Qdhw_name_prefix, Ttank_name_prefix, min_temp_preference_param, max_temp_preference_param)

**Module:** ``flexgridpy.electrical_models.variables.def_tank_var``

.. code-block:: python

   initialize_tank_flexibility_variables(manager, model_type, Qdhw_upward_name_prefix, Qdhw_downward_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_tank_var``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_tank_variables(...)

Description
-----------

Creates DHW tank temperature and thermal power variables for the stirred-tank
thermodynamic model.

Variables Created
-----------------

* ``Ttank[i, t]`` — tank water temperature (°C)
* ``Qtank[i, t]`` — thermal power delivered to tank (kW)
* Flexibility variables for tank thermal flexibility (optional)


See Also
--------

* :doc:`../constraints_hp_dhw/add_tank_thermodynamic_constraint`
* :doc:`../parameters/initialize_tank_params`
