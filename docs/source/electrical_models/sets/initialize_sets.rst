initialize_sets
===============

Description
-----------

Initializes all core Pyomo sets from the pandapower network and from flex-asset
tables (EV, HP, tank) stored in :class:`~flexgridpy.electrical_models.initializations.additional_data.AdditionalData`.

This function must be called **before** adding parameters or variables.

Sets Created
------------

From pandapower ``net``
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Set name
     - Description
   * - ``Sbuses``
     - All bus indices (``net.bus``)
   * - ``SGrid``
     - External grid connection buses (``net.ext_grid``)
   * - ``SDER_contr``
     - Controllable distributed generators (``net.sgen``, Controllable=True)
   * - ``SDER_uncontr``
     - Uncontrollable RES (``net.sgen``, Controllable=False)
   * - ``SLoadbuses``
     - Buses with loads (``net.load['bus']``)
   * - ``Slines``
     - Directed line pairs ``(from_bus, to_bus)``
   * - ``STransformers``
     - Directed transformer pairs ``(from_bus, to_bus)``
   * - ``STimes``
     - Time steps: ``range(timeframe * 60 / time_interval)``

Topology helper sets
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Set name
     - Description
   * - ``Sdownstream[j]``
     - Buses reachable downstream of bus ``j`` via lines
   * - ``Supstream[j]``
     - Buses directly upstream of bus ``j`` via lines
   * - ``Sdownstream_transformer[j]``
     - Downstream transformers from bus ``j``
   * - ``Supstream_transformer[j]``
     - Upstream transformers to bus ``j``

Flex-asset sets
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Set name
     - Description
   * - ``SEVbuses``
     - Buses with electric vehicles (manual input via ``addEV``)
   * - ``SHPbuses``
     - Buses with heat pumps
   * - ``STankbuses``
     - Buses with DHW thermal tanks
   * - ``SDistance_ind``
     - Index set for multiple departure events per EV

Time index
----------

The time set is computed as:

.. math::

   \mathcal{T} = \{0, 1, \ldots, T-1\}, \quad T = \frac{\text{timeframe} \times 60}{\text{time\_interval}}

where ``timeframe`` is in hours and ``time_interval`` is in minutes.

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.sets.sets.initialize_sets

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_sets

Example
-------

.. code-block:: python

   mgr.addTime(timeframe=24, time_interval=60)   # 24 h, 1 h steps → STimes = {0,...,23}
   mgr.initialize_sets()
   print(mgr.list_sets())
