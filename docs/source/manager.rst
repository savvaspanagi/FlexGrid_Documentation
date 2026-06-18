Manager
=======

The :class:`~flexgridpy.electrical_models.Manager.Manager` class is the **central
entry point** for building and solving FlexGridPy optimization problems. It wraps
a pandapower ``net`` object and provides a unified API for electrical models,
market clearing, and result handling.

Although the Manager lives in ``flexgridpy.electrical_models``, it is documented
separately.

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
        └── ...           → other components
        

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

The Manager maintains four registries for inspecting the built model (Similar with any other optimization model):

* ``constraint_registry`` — registered Pyomo constraint groups
* ``set_registry`` — registered Pyomo sets
* ``variable_registry`` — registered Pyomo variables
* ``parameter_registry`` — registered Pyomo parameters

For viewing the registries names:
* :meth:`~flexgridpy.electrical_models.Manager.Manager.list_sets()`
* :meth:`~flexgridpy.electrical_models.Manager.Manager.list_variables()`
* :meth:`~flexgridpy.electrical_models.Manager.Manager.list_parameters()`
* :meth:`~flexgridpy.electrical_models.Manager.Manager.list_constraints()`

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
