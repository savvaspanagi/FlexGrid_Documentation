Heat Pump & DHW Constraints
===========================

Thermal constraints for heat pumps, building envelopes (3R2C), and domestic
hot water (DHW) stirred-tank models.

Building Thermodynamics
-----------------------

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_thermodynamic_constr.add_building_thermodynamic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_flexibility_constr.add_building_thermodynamic_flexibility_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_thermodynamic_constr.add_building_thermodynamic_stochastic_constraint

Heat Pump Operation
-------------------

.. autofunction:: flexgridpy.electrical_models.constraints.hp.hp_operation_constr.add_HP_operation_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.hp_operation_constr.add_HP_operation_stochastic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.hp_flex_operation_constr.add_HP_flex_sh_operation_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.hp_flex_operation_constr.add_HP_flex_tank_operation_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.hp.building_3R2C_thermodynamic_constr.add_Qhp_gamma_valve_limit_constraint

DHW Tank Thermodynamics
-----------------------

.. autofunction:: flexgridpy.electrical_models.constraints.dhw.stirred_tank_thermodynamic_constr.add_tank_thermodynamic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.dhw.stirred_tank_thermodynamic_flex_constr.add_tank_flexibility_thermodynamic_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.dhw.stirred_tank_thermodynamic_constr.add_Qtank_gamma_valve_limit_constraint

Transformer (Stochastic)
------------------------

.. autofunction:: flexgridpy.electrical_models.constraints.transformer.transf_stochastic_constr.add_active_power_flow_transformer_stochastic_constraint

Example
-------

.. code-block:: python

   mgr.initialize_hp_params()
   mgr.enviroment_profile_param()
   mgr.initialize_hp_variables()
   mgr.initialize_building_variables()
   mgr.add_building_thermodynamic_constraint()
   mgr.add_HP_operation_constraint()
