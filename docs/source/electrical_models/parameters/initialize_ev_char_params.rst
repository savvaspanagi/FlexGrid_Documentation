initialize_ev_char_params
=========================

Description
-----------

Registers EV user-behavior parameters: arrival/departure times, trip distances,
minimum departure SOC, trip energy needs, and charging availability windows.

Parameters Registered
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Prefix
     - Content
   * - ``ev_arrival_prefix_name``
     - Arrival time index per EV and trip event
   * - ``ev_departure_prefix_name``
     - Departure time index per EV and trip event
   * - ``ev_distance_prefix_name``
     - Trip distance (km) per event
   * - ``EV_SoC_min_departure_prefix_name``
     - Minimum SOC (%) required at departure
   * - ``ev_trip_energy_needs_prefix_name``
     - Energy consumed per trip (p.u.·h)
   * - ``ev_availability_prefix_name``
     - Binary availability flag (1 = plugged in)

Trip Energy
-----------

At each departure event :math:`x`, the SoC is reduced by the trip energy need:

.. math::

   E_{i,t_\text{arr}-1} = E_{i,t_\text{arr}-2} - E_{i,x}^\text{trip}

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.parameters.ev_char_param_fun.initialize_ev_char_params

.. autofunction:: flexgridpy.electrical_models.parameters.ev_char_param_fun.initialize_ev_char_stochastic_params

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_ev_char_params

See Also
--------

* :doc:`../constraints_ev/add_ev_soc_constraint`
