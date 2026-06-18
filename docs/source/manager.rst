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

* ``mgr.list_constraints()`` — registered Pyomo constraint groups
* ``mgr.list_sets()`` — registered Pyomo sets
* ``mgr.list_variables()`` — registered Pyomo variables
* ``mgr.list_parameters()`` — registered Pyomo parameters

Sub-components
--------------

On initialization, the Manager also creates:

* ``mgr.anc_Vars`` — :class:`~flexgridpy.electrical_models.initializations.additional_data.AdditionalData` - 
* ``mgr.market`` — :class:`~flexgridpy.market_models.manager_market.MarketAPI`
* ``mgr.plot_fun`` — plotting utilities

After problem solved, using manual function calls, the Manager also creates:

* ``mgr.results`` — result DataFrame utilities
* ``mgr.parameter_df`` — parameter DataFrame utilities
