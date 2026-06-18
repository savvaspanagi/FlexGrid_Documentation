EV Constraints
==============

Electric vehicle constraints model battery state-of-charge dynamics, departure
requirements, charging/discharging limits, and upward/downward flexibility.

State of Charge
---------------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_soc_cons.add_ev_soc_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons.add_ev_min_departure_soc_constraint

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons.add_ev_min_custom_departure_soc_constraint

Charging / Discharging
----------------------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_power_dp.add_power_ch_dp_ev_cons

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_avoid_cha_unconn_cons.fix_ev_non_charging_times

Flexibility
-----------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_up_flex_ev_cons

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_up_flex_max_cons

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_down_flex_ev_cons

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_flexibility_cons.add_power_down_flex_min_cons

Stochastic EV Constraints
-------------------------

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_soc_cons.add_ev_soc_constraint_stochastic

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_avoid_cha_unconn_cons.fix_ev_non_charging_times_stochastic

.. autofunction:: flexgridpy.electrical_models.constraints.ev.ev_min_soc_cons.add_ev_min_custom_departure_soc_stochastic_constraint

Example
-------

.. code-block:: python

   mgr.initialize_ev_params()
   mgr.initialize_ev_char_params()
   mgr.initialize_ev_variables()
   mgr.add_ev_soc_constraint()
   mgr.add_ev_min_departure_soc_constraint()
   mgr.fix_ev_non_charging_times()
