Sets
====

Pyomo sets define the indexing structure of the optimization model. Sets are
created from the pandapower ``net`` tables and from manually added flex assets
(EVs, heat pumps, tanks).

Initialize Sets
---------------

.. autofunction:: flexgridpy.electrical_models.sets.sets.initialize_sets

Stochastic Set
--------------

.. autofunction:: flexgridpy.electrical_models.sets.sets.add_stochastic_set

Set Overview
------------

``initialize_sets`` creates the following sets from the pandapower network:

**Sbuses**
   All bus indices (net.bus)

**SGrid**
   External grid buses (net.ext_grid)

**SDER_contr / SDER_uncontr**
   Controllable / uncontrollable DER (net.sgen)

**SLoadbuses**
   Buses with loads (net.load)

**Slines / STransformers**
   Network lines and transformers (from, to pairs)

**STimes**
   Simulation time steps

**Sdownstream / Supstream**
   Downstream / upstream buses per bus

**SEVbuses / SHPbuses / STankbuses**
   Buses with EVs, heat pumps, or thermal tanks (manual input)

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_sets
.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_stochastic_set
