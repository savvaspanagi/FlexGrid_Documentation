initialize_sets
===============

Function
--------

.. code-block:: python

   initialize_sets(manager)

**Module:** ``flexgridpy.electrical_models.sets.sets``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_sets(...)

Description
-----------

Initializes all core Pyomo sets from the pandapower network and flex-asset tables.
Must be called before adding parameters or variables.

Creates bus, line, transformer, DER, load, EV, HP, tank, and time sets from
the pandapower ``net`` and :class:`~flexgridpy.electrical_models.initializations.additional_data.AdditionalData`.

Time index
~~~~~~~~~~

Call :doc:`../variables/addTime` **first** to define the simulation horizon.
``initialize_sets`` then builds ``STimes`` from that configuration:

.. math::

   \mathcal{T} = \{0, 1, \ldots, T-1\}, \quad
   T = \frac{\text{timeframe} \times 60}{\text{time\_interval}}

Sets Created
~~~~~~~~~~~~

**Sbuses** — all bus indices  
**SGrid** — external grid buses  
**SDER_contr / SDER_uncontr** — controllable / uncontrollable DER  
**SLoadbuses** — load buses  
**Slines / STransformers** — branch pairs  
**STimes** — time steps (from the time index above)  
**SEVbuses / SHPbuses / STankbuses** — flex assets

Example
-------

.. code-block:: python

   mgr.addTime(timeframe=24, time_interval=60)
   mgr.initialize_sets()
   print(mgr.list_sets())
