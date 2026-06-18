add_real_current_flow_constraint
================================

Function
--------

.. code-block:: python

   add_real_current_flow_constraint(manager, model_set, current_flow_constr_name_prefix, active_curr_var, voltage_var, phase_angle_var)

**Module:** ``flexgridpy.electrical_models.constraints.flow.current_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_real_current_flow_constraint(...)

Adds real current flow constraints.

Example
-------

.. code-block:: python

   mgr.add_real_current_flow_constraint()
