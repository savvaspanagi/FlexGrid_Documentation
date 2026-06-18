add_power_up_flex_ev_cons
==========================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_up_flex_ev_cons

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_up_flex_max_cons

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.add_power_up_flex_ev_cons

Description
-----------

Limits **upward flexibility** (additional charging headroom) based on the
remaining battery capacity.

Mathematical Formulation
------------------------

.. math::

   E_{i,t-1} + \left(p_{i,t}^{\uparrow,\text{flex}} + p_{i,t}^\text{ch}\right) \cdot \Delta t \leq E_{i}^\max

Companion constraint ``add_power_up_flex_max_cons`` additionally enforces:

.. math::

   p_{i,t}^{\uparrow,\text{flex}} + p_{i,t}^\text{ch} \leq \overline{P}_\text{ch}





See Also
--------

* :doc:`add_power_down_flex_ev_cons`
