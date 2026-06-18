initialize_sets
===============

Initializes all core Pyomo sets from the pandapower network and flex-asset tables.
Must be called before adding parameters or variables.

Function
--------

.. autofunction:: flexgridpy.electrical_models.sets.sets.initialize_sets

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_sets

Description
-----------

Creates bus, line, transformer, DER, load, EV, HP, tank, and time sets from
the pandapower ``net`` and :class:`~flexgridpy.electrical_models.initializations.additional_data.AdditionalData`.

Sets Created
~~~~~~~~~~~~

**Sbuses** — all bus indices | **SGrid** — external grid buses |
**SDER_contr / SDER_uncontr** — controllable / uncontrollable DER |
**SLoadbuses** — load buses | **Slines / STransformers** — branch pairs |
**STimes** — time steps | **SEVbuses / SHPbuses / STankbuses** — flex assets

Time index
~~~~~~~~~~

.. math::

   \mathcal{T} = \{0, 1, \ldots, T-1\}, \quad
   T = \frac{\text{timeframe} \times 60}{\text{time\_interval}}

Example
-------

.. code-block:: python

   mgr.addTime(timeframe=24, time_interval=60)
   mgr.initialize_sets()
   print(mgr.list_sets())
