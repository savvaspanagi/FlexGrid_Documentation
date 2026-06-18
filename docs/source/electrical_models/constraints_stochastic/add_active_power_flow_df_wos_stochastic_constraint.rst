add_active_power_flow_df_wos_stochastic_constraint
==================================================

Function
--------

.. code-block:: python

   add_active_power_flow_df_wos_stochastic_constraint(manager, pder_contrl_var, pline_var, p_transformer_var, pgrid_var, line_current_var, transformer_current_var, name_prefix, ev_ch_p_var=None, p_hp_var=None)

**Module:** ``flexgridpy.electrical_models.constraints.pf.distflow_wo_shunt_stochastic_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_active_power_flow_df_wos_stochastic_constraint(...)

Stochastic DistFlow active power balance.

Example
-------

.. code-block:: python

   mgr.add_active_power_flow_df_wos_stochastic_constraint()
