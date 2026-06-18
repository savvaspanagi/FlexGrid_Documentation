Variables
=========

Decision variables in the Pyomo optimization model. Variables are registered
via ``manager.register_variable(name, var)``.

.. toctree::
   :maxdepth: 1

   variables/addTime
   variables/initialize_voltage_square_variables
   variables/initialize_branch_square_variables
   variables/initialize_der_variables
   variables/initialize_ev_variables
   variables/initialize_ev_flexibility_variables
   variables/initialize_hp_variables
   variables/initialize_building_variables
   variables/initialize_tank_variables

Additional Variables
--------------------

The following are documented via API reference in the source modules:

* :func:`~flexgridpy.electrical_models.variables.def_voltage_var.initialize_voltage_variables` — AC voltage magnitude and angle
* :func:`~flexgridpy.electrical_models.variables.def_line_var.initialize_branch_variables` — AC branch P/Q flows
* :func:`~flexgridpy.electrical_models.variables.def_transformer_var.initialize_transformer_variables` — Transformer flows
* :func:`~flexgridpy.electrical_models.variables.def_var.add_variable` — Custom user-defined variable
* Stochastic variants — append ``_stochastic`` suffix to variable initialization functions
