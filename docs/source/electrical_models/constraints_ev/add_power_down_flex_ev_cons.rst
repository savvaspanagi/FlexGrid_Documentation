add_power_down_flex_ev_cons
============================

Function
--------

.. code-block:: python

   add_power_down_flex_ev_cons(manager, name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons``

.. code-block:: python

   add_power_down_flex_min_cons(manager, name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons``

Manager Method
--------------

.. code-block:: python

   mgr.add_power_down_flex_ev_cons(...)

Description
-----------

Limits **downward flexibility** (reduced charging / discharging headroom) based
on the minimum required SoC at each time step.

Mathematical Formulation
------------------------

.. math::

   E_{i,t-1} + \left(p_{i,t}^\text{ch} - p_{i,t}^{\downarrow,\text{flex}}\right) \cdot \Delta t \geq E_{i,t}^\min

Companion constraint ``add_power_down_flex_min_cons`` enforces:

.. math::

   p_{i,t}^{\downarrow,\text{flex}} \leq p_{i,t}^\text{ch}


See Also
--------

* :doc:`add_power_up_flex_ev_cons`
