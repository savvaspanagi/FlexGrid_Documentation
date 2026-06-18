Manager
=======

The :class:`~flexgridpy.electrical_models.Manager.Manager` class is the main entry
point for building and solving electrical optimization problems. It wraps a
pandapower ``net`` object and exposes methods to register Pyomo sets, parameters,
variables, and constraints.

Create Function
---------------

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
   mgr.line_param()

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
