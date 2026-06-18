add_power_ch_dp_ev_cons
========================

Function
--------

.. code-block:: python

   add_power_ch_dp_ev_cons(manager, name_prefix)

**Module:** ``flexgridpy.electrical_models.constraints.ev.ev_power_dp``

Manager Method
--------------

.. code-block:: python

   mgr.add_power_ch_dp_ev_cons(...)

Description
-----------

Constrains EV charging/discharging power to stay within the inverter limits
and enforces the sign convention for charging vs. discharging.

Mathematical Formulation
------------------------

.. math::

   \underline{P}_\text{ch} \leq p_{i,t}^\text{ch} \leq \overline{P}_\text{ch}
