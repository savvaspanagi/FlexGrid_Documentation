add_line_flow_amplitude_losses_stochastic_constraint
====================================================

Function
--------

.. code-block:: python

   add_line_flow_amplitude_losses_stochastic_constraint(manager, resistance_param, line_set, current_var, losses_var, line_flow_losses_con_name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.line.line_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_line_flow_amplitude_losses_stochastic_constraint(...)

Stochastic line amplitude loss constraints.

Example
-------

.. code-block:: python

   mgr.add_line_flow_amplitude_losses_stochastic_constraint()
