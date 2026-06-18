DistFlow Constraints
====================

DistFlow (without shunt) is the default convex OPF formulation for radial
distribution networks. FlexGridPy implements the full set of active/reactive
power flow, voltage drop, and branch current constraints, with both exact
and SOCP relaxations.

Active Power Flow
-----------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_active_power_flow_df_wos_constraint

Reactive Power Flow
-------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_reactive_power_flow_df_wos_constraint

Voltage Drop
------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_voltage_power_flow_df_wos_constraint

Branch Current (Exact)
----------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_brunch_current_flow_df_wos_equal_constraint

Branch Current (SOCP)
---------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.add_brunch_current_flow_df_wos_SOCP_constraint

SOCP Exactness Check
--------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_constr.check_socp_exactness

Example
-------

.. code-block:: python

   mgr.initialize_voltage_square_variables()
   mgr.initialize_branch_square_variables()
   mgr.add_active_power_flow_df_wos_constraint()
   mgr.add_reactive_power_flow_df_wos_constraint()
   mgr.add_voltage_power_flow_df_wos_constraint()
   mgr.add_brunch_current_flow_df_wos_SOCP_constraint()
