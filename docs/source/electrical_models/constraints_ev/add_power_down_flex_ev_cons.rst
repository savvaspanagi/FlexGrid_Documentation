add_power_down_flex_ev_cons
============================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_down_flex_ev_cons

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_down_flex_min_cons

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_power_down_flex_ev_cons

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
