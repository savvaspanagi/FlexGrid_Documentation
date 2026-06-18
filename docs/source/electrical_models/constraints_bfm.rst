Branch Flow Model (BFM)
=======================

The Branch Flow Model provides an alternative OPF formulation with explicit
current and voltage-drop equations, suitable for radial networks with shunt
elements and tap changers.

.. toctree::
   :maxdepth: 1

   constraints_bfm/add_active_power_flow_bfm
   constraints_bfm/add_voltage_drop_bfm
   constraints_bfm/add_current_flow_bfm

Additional Functions
--------------------

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_reactive_power_flow_bfm

.. autofunction:: flexgridpy.electrical_models.constraints.pf.BFM_wshunt_radial_constr.add_voltage_link_symmetric_constraint

Prerequisites
-------------

Call :doc:`../parameters/alpha_bfm_param` before adding BFM voltage-drop constraints.
