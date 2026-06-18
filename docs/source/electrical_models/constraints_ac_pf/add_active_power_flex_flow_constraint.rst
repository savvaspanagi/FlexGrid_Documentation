add_active_power_flex_flow_constraint
=====================================

Function
--------

.. code-block:: python

   add_active_power_flex_flow_constraint(manager, pder_contrl_var, pgrid_var, ev_ch_p_var, ev_flex_p_var, voltage_v_var, voltage_pa_var, name_prefix, type, p_hp_var=None)

**Module:** ``flexgridpy.electrical_models.constraints.pf.full_ac_pf_flex_constr``

Manager Method
--------------

.. code-block:: python

   mgr.add_active_power_flex_flow_constraint(...)

Adds flexibility-aware AC active power flow constraints.

Example
-------

.. code-block:: python

   mgr.add_active_power_flex_flow_constraint()
