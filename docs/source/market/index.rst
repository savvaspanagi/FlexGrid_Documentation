Market Models
=============

FlexGridPy provides modular market-clearing formulations built on top of the
electrical :class:`~flexgridpy.electrical_models.Manager.Manager`. Markets are
accessed via ``manager.market`` (:class:`~flexgridpy.market_models.manager_market.MarketAPI`).

Two clearing modes are supported:

* **Copperplate** — aggregated supply/demand balance without network constraints.
* **DC-OPF market** — locational clearing with DC power flow constraints.

.. toctree::
   :maxdepth: 2
   :caption: Market Models

   market/overview
   market/api
   market/inputs
   market/formulation
   market/constraints
   market/objective

Quick Links
-----------

* :doc:`market/api` — :class:`MarketAPI` reference
* :doc:`market/inputs` — Prepare offers, bids, and demand profiles
* :doc:`market/formulation` — Build copperplate or DC-OPF market models
* :doc:`market/constraints` — Generation limits and DC network constraints
