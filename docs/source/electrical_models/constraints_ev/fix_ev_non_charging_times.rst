fix_ev_non_charging_times
==========================

Function
--------

.. code-block:: python

   fix_ev_non_charging_times(manager, model_ev_ch=None, model_ev_flex_up=None, model_ev_flex_down=None)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_avoid_cha_unconn_cons``

.. code-block:: python

   fix_ev_non_charging_times_stochastic(manager, model_stochastic_pev_ch=None, model_stochastic_qev_ch=None)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_avoid_cha_unconn_cons``

Manager Method
--------------

.. code-block:: python

   mgr.fix_ev_non_charging_times(...)

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
