Branch Flow Model (BFM)
=======================

The Branch Flow Model provides an alternative OPF formulation with explicit
current and voltage-drop equations, suitable for radial networks with shunt
elements.

Active Power Flow
-----------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_active_power_flow_bfm

Reactive Power Flow
-------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_reactive_power_flow_bfm

Voltage Drop
------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_voltage_drop_bfm

Current Flow
------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_current_flow_bfm

Voltage Link Symmetry
---------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_voltage_link_symmetric_constraint

Example
-------

.. code-block:: python

   mgr.alpha_bfm_param()
   mgr.initialize_voltage_square_variables()
   mgr.initialize_branch_square_variables()
   mgr.add_active_power_flow_bfm()
   mgr.add_reactive_power_flow_bfm()
   mgr.add_voltage_drop_bfm()
   mgr.add_current_flow_bfm()
