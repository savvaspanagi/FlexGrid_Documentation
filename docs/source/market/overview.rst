Market Overview
===============

The market module formulates electricity market clearing problems as Pyomo
optimization models. It supports:

* Time-indexed generator offers and demand profiles
* Optional bid-side demand response units
* Optional unit commitment (on/off) binaries
* Copperplate clearing (no network)
* DC-OPF clearing with line flow and nodal balance constraints

Workflow
--------

1. Prepare market inputs with :func:`~flexgridpy.market_models.initializations.io.prepare_market_inputs`.
2. Build the model with :func:`~flexgridpy.market_models.initializations.formulation.formulate_copperplate_market`
   or :func:`~flexgridpy.market_models.initializations.formulation.formulate_dc_opf_market`.
3. Solve with a Pyomo-compatible solver.

Example (Copperplate)
---------------------

.. code-block:: python

   import pandas as pd
   import pandapower as pp
   from flexgridpy.electrical_models.Manager import Manager
   from flexgridpy.market_models.initializations.io import prepare_market_inputs
   from flexgridpy.market_models.initializations.formulation import formulate_copperplate_market

   net = pp.create_empty_network()
   mgr = Manager(net)

   offers_df = pd.DataFrame({
       "unit": ["G1", "G2"],
       "pmin": [0, 0],
       "pmax": [100, 50],
       "price": [30, 45],
   })
   demand_df = pd.DataFrame({"time": range(24), "demand": [80] * 24})

   market_inputs = prepare_market_inputs(mgr, offers_df, demand_profile_df=demand_df)
   formulate_copperplate_market(mgr, market_inputs)

Example (DC-OPF Market)
-----------------------

.. code-block:: python

   from flexgridpy.market_models.initializations.formulation import formulate_dc_opf_market

   # Requires a populated pandapower net with lines and ext_grid
   market_inputs = prepare_market_inputs(
       mgr, offers_df, demand_profile_df=demand_df, unit_bus_map={"G1": 0, "G2": 1}
   )
   formulate_dc_opf_market(mgr, market_inputs)
