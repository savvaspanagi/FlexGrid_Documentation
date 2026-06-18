MarketAPI
=========

The :class:`~flexgridpy.market_models.manager_market.MarketAPI` class is attached
to every :class:`~flexgridpy.electrical_models.Manager.Manager` instance as
``manager.market``. It provides modular methods to build market models step by step.

.. autoclass:: flexgridpy.market_models.manager_market.MarketAPI
   :members:
   :undoc-members: False
   :show-inheritance:

Access
------

.. code-block:: python

   mgr = Manager(net)
   mgr.market.prepare_inputs(offers_df, demand_profile_df=demand_df)
   mgr.market.initialize_market_sets(market_inputs)
   mgr.market.initialize_market_parameters(market_inputs)
