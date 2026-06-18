Market Inputs
=============

Prepare time-indexed market inputs from pandas DataFrames.

.. autofunction:: flexgridpy.market_models.initializations.io.prepare_market_inputs

Input DataFrames
----------------

**offers_df** (required)
   Generator offers with columns: ``unit``, ``pmin``, ``pmax``, ``price``.

**demand_profile_df** (optional)
   System demand profile with ``time`` and ``demand`` columns.

**bids_df** (optional)
   Demand-side bid units with ``unit``, ``pmin``, ``pmax``, ``price``.

**unit_bus_map** (required for DC-OPF)
   Dictionary mapping generator unit names to pandapower bus indices.

Example
-------

.. code-block:: python

   import pandas as pd

   offers_df = pd.DataFrame({
       "unit": ["G1", "G2"],
       "pmin": [0, 0],
       "pmax": [100, 50],
       "price": [30, 45],
   })
   demand_df = pd.DataFrame({
       "time": list(range(24)),
       "demand": [80.0] * 24,
   })

   market_inputs = mgr.market.prepare_inputs(
       offers_df,
       demand_profile_df=demand_df,
   )

Market Sets
-----------

.. autofunction:: flexgridpy.market_models.sets.init_set.initialize_market_sets

Market Parameters
-----------------

.. autofunction:: flexgridpy.market_models.parameters.init_parameter.initialize_market_parameters

.. autofunction:: flexgridpy.market_models.parameters.init_parameter.initialize_market_bus_mapping_parameters

.. autofunction:: flexgridpy.market_models.parameters.dc_market_param.initialize_dc_market_line_parameters

Market Variables
----------------

.. autofunction:: flexgridpy.market_models.variables.init_variable.initialize_market_variables

.. autofunction:: flexgridpy.market_models.variables.dc_market_var.initialize_dc_market_variables
