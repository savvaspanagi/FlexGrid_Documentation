fix_ev_non_charging_times
==========================



Function
--------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_avoid_cha_unconn_cons.fix_ev_non_charging_times

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_avoid_cha_unconn_cons.fix_ev_non_charging_times_stochastic

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.fix_ev_non_charging_times

Description
-----------

Forces EV charging and flexibility power to **zero** when the vehicle is not
connected to the charging point (unavailable periods).

Mathematical Formulation
------------------------

When ``ev_availability[i, t] = 0``:

.. math::

   p_{i,t}^\text{ch} = 0, \quad p_{i,t}^{\uparrow,\text{flex}} = 0, \quad p_{i,t}^{\downarrow,\text{flex}} = 0

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Argument
     - Description
   * - ``model_ev_ch`` (optional)
     - EV charging power variable
   * - ``model_ev_flex_up`` (optional)
     - Upward flexibility variable
   * - ``model_ev_flex_down`` (optional)
     - Downward flexibility variable
