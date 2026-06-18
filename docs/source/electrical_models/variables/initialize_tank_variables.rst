initialize_tank_variables
=========================



Function
--------

.. autofunction:: flexgridpy.electrical_models.variables.def_tank_var.initialize_tank_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_tank_var.initialize_tank_flexibility_variables

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_tank_variables

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
