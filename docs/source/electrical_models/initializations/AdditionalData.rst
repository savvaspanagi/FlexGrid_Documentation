AdditionalData
==============

Converts the pandapower ``net`` into per-unit DataFrames compatible with the
optimization model.

Class
-----

.. autoclass:: flexgridpy.electrical_models.initializations.additional_data.AdditionalData
   :members:
   :undoc-members: False
   :show-inheritance:

Example
-------

.. code-block:: python

   mgr = Manager(net)
   mgr.anc_Vars.addEV(ev_dataframe)
   mgr.anc_Vars.addFlexBuilding(hp_dataframe)
