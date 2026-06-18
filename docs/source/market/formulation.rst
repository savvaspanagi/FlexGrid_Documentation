Market Formulation
==================

High-level functions to build complete market models in one call.

Copperplate Market
------------------

Time-indexed copperplate clearing without network constraints.

.. autofunction:: flexgridpy.market_models.initializations.formulation.formulate_copperplate_market

DC-OPF Market
-------------

Locational clearing with DC power flow constraints on the distribution network.

.. autofunction:: flexgridpy.market_models.initializations.formulation.formulate_dc_opf_market

When to Use Which
-----------------

**Copperplate** — No network constraints needed; fast aggregated clearing.

**DC-OPF market** — Locational prices and line limits matter; uses network constraints.
