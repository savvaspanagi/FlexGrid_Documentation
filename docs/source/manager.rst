Manager
=======

The :class:`~flexgridpy.electrical_models.Manager.Manager` class is the **central
entry point** for building and solving FlexGridPy optimization problems. It wraps
a pandapower ``net`` object and provides a unified API for electrical models,
market clearing, and result handling.

Although the Manager lives in ``flexgridpy.electrical_models``, it is documented
separately because it orchestrates multiple modules — including
:doc:`market/index` via ``mgr.market``.

Architecture
------------

.. code-block:: text

   pandapower net
        │
        ▼
   Manager(net)
        ├── anc_Vars      → network DataFrames (per-unit)
        ├── market        → MarketAPI (copperplate / DC-OPF market)
        ├── plot_fun      → result plotting
        ├── results       → variable → DataFrame export
        └── parameter_df  → parameter → DataFrame export

Function
--------

.. autoclass:: flexgridpy.electrical_models.Manager.Manager
   :members:
   :undoc-members: False
   :show-inheritance:
   :special-members: __init__

Example
-------

.. code-block:: python

   import pandapower as pp
   from flexgridpy.electrical_models.Manager import Manager

   net = pp.networks.case33bw()
   mgr = Manager(net)
   mgr.initialize_sets()
   mgr.line_param(Y_bus, ...)

Registry Utilities
------------------

The Manager maintains four registries for inspecting the built model:

* ``constraint_registry`` — registered Pyomo constraint groups
* ``set_registry`` — registered Pyomo sets
* ``variable_registry`` — registered Pyomo variables
* ``parameter_registry`` — registered Pyomo parameters

Use :meth:`~flexgridpy.electrical_models.Manager.Manager.list_constraints`,
:meth:`~flexgridpy.electrical_models.Manager.Manager.list_variables`, etc. to
inspect the model after building.

Sub-components
--------------

On initialization, the Manager also creates:

* ``mgr.anc_Vars`` — :class:`~flexgridpy.electrical_models.initializations.additional_data.AdditionalData`
* ``mgr.market`` — :class:`~flexgridpy.market_models.manager_market.MarketAPI`
* ``mgr.plot_fun`` — plotting utilities
* ``mgr.results`` — result extraction utilities
* ``mgr.parameter_df`` — parameter DataFrame utilities

See Also
--------

* :doc:`electrical_models/index` — sets, parameters, variables, constraints
* :doc:`market/index` — market clearing via ``mgr.market``
