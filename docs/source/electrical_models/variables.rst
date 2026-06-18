Variables
=========

Variables represent the decision quantities in the optimization model:
voltages, branch flows, DER dispatch, EV charging power, and thermal states.

Time
----

.. autofunction:: flexgridpy.electrical_models.variables.time_manager.addTime

Voltage Variables
-----------------

.. autofunction:: flexgridpy.electrical_models.variables.def_voltage_var.initialize_voltage_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_voltage_var.initialize_voltage_square_variables

Branch Variables
----------------

.. autofunction:: flexgridpy.electrical_models.variables.def_line_var.initialize_branch_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_line_var.initialize_branch_square_variables

DER Variables
-------------

.. autofunction:: flexgridpy.electrical_models.variables.def_der_var.initialize_der_variables

EV Variables
------------

.. autofunction:: flexgridpy.electrical_models.variables.def_ev_var.initialize_ev_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_ev_flex.initialize_ev_flexibility_variables

Transformer Variables
---------------------

.. autofunction:: flexgridpy.electrical_models.variables.def_transformer_var.initialize_transformer_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_transformer_var.initialize_transformer_square_variables

Heat Pump & Building Variables
------------------------------

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_hp_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_gamma_valve_variable

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_hp_flex_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_building_var.initialize_building_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_building_var.initialize_building_flex_variables

Tank Variables
--------------

.. autofunction:: flexgridpy.electrical_models.variables.def_tank_var.initialize_tank_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_tank_var.initialize_tank_flexibility_variables

Custom Variables
----------------

.. autofunction:: flexgridpy.electrical_models.variables.def_var.add_variable

Stochastic Variables
--------------------

.. autofunction:: flexgridpy.electrical_models.variables.def_voltage_var.initialize_voltage_stochastic_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_voltage_var.initialize_voltage_square_stochastic_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_var.add_stochastic_variable

.. autofunction:: flexgridpy.electrical_models.variables.def_var.add_aggregated_stochastic_variable

.. autofunction:: flexgridpy.electrical_models.variables.def_line_var.initialize_branch_stochastic_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_line_var.initialize_branch_square_stochastic_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_hp_var.initialize_hp_stochastic_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_building_var.initialize_building_stochastic_variables

.. autofunction:: flexgridpy.electrical_models.variables.def_ev_var.initialize_ev_variables_stochastic

.. autofunction:: flexgridpy.electrical_models.variables.def_der_var.initialize_der_stochastic_variables

Surrogate Variables
-------------------

.. autofunction:: flexgridpy.electrical_models.variables.def_nn_var.initialize_int_nn_surrogate_variables
