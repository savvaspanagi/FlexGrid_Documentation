Heat Pump & DHW Constraints
=============================

Thermal constraints for heat pumps, 3R2C building envelopes, and stirred-tank DHW models.

.. toctree::
   :maxdepth: 1

   constraints_hp_dhw/add_building_thermodynamic_constraint
   constraints_hp_dhw/add_HP_operation_constraint
   constraints_hp_dhw/add_tank_thermodynamic_constraint

Additional Functions
--------------------

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_thermodynamic_constr.add_Qhp_gamma_valve_limit_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_flexibility_constr.add_building_thermodynamic_flexibility_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.hp_flex_operation_constr.add_HP_flex_sh_operation_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.hp_flex_operation_constr.add_HP_flex_tank_operation_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.dhw.stirred_tank_thermodynamic_flex_constr.add_tank_flexibility_thermodynamic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.dhw.stirred_tank_thermodynamic_constr.add_Qtank_gamma_valve_limit_constraint
