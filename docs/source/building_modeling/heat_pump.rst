Heat Pump Model
===============

COP regression model for converting thermal demand to electrical power.

.. autoclass:: flexgridpy.thermal_models.HP_Operation.hp_model.HeatPumpModel
   :members:
   :undoc-members: False
   :show-inheritance:

Convert Heat Demand to Power
----------------------------

.. autofunction:: flexgridpy.thermal_models.HP_Operation.demand_converter.convert_heat_demand_to_power_series

Example
-------

.. code-block:: python

   from flexgridpy.thermal_models.HP_Operation.hp_model import HeatPumpModel

   hp = HeatPumpModel(cop_coeffs=[6.0, -0.1, -0.05])
   cop = hp.compute_cop(delta_T=30.0)
   print(f"COP at delta_T=30°C: {cop:.2f}")

   hp.generate_cop_curve(delta_T_range=(10, 50))
