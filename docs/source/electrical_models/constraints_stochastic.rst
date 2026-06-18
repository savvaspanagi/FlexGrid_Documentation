Stochastic Constraints
======================

Scenario-indexed constraints for uncertainty-aware optimization. These extend
the deterministic DistFlow and line-loss formulations across multiple scenarios.

DistFlow (Stochastic)
---------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr.add_active_power_flow_df_wos_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr.add_reactive_power_flow_df_wos_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr.add_voltage_power_flow_df_wos_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr.add_brunch_current_flow_df_wos_equal_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr.add_brunch_current_flow_df_wos_SOCP_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr.check_socp_exactness_stochastic

Line Losses (Stochastic)
------------------------

.. autofunction:: flexgridpy.electrical_models.constraints.line.line_constr.add_line_flow_losses_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.line.line_constr.add_line_flow_amplitude_losses_stochastic_constraint

Example
-------

.. code-block:: python

   mgr.add_stochastic_set(n_scenarios=5)
   mgr.add_stochastic_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
   mgr.initialize_voltage_square_stochastic_variables()
   mgr.add_active_power_flow_df_wos_stochastic_constraint()
