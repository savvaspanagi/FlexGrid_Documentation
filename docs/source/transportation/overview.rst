Transportation Overview
=======================

The transportation module supports probabilistic generation of EV-related data
such as daily trip distances. These generated profiles feed into the electrical
optimization model via:

* :func:`~flexgridpy.electrical_models.parameters.ev_char_param_fun.initialize_ev_char_params`
* :func:`~flexgridpy.electrical_models.initializations.ev_conv_profiles.generate_conventional_ev_profiles`

Workflow
--------

1. **Sample trip distances** using truncated probability distributions.
2. **Convert distances to energy needs** based on EV efficiency.
3. **Pass arrival/departure times and energy needs** to the EV parameter functions.
4. **Build EV constraints** in the electrical optimization model.

Example Pipeline
----------------

.. code-block:: python

   import numpy as np
   from flexgridpy.transportation_models.ev_probabilistic.truncated_t_samples import truncated_t_sample

   # Sample 100 daily trip distances (km) from a truncated t-distribution
   distances = truncated_t_sample(
       df=5, loc=25.0, scale=8.0, a=2.0, b=80.0, size=100
   )

   # Convert to energy needs (kWh) assuming 0.2 kWh/km
   energy_needs = distances * 0.2

   # Use in EV parameter initialization
   mgr.initialize_ev_char_params(
       ev_arrival_prefix_name="EV_arr",
       ev_departure_prefix_name="EV_dep",
       ev_distance_prefix_name="EV_dist",
       EV_SoC_min_departure_prefix_name="EV_soc_min",
       ev_trip_energy_needs_prefix_name="EV_energy",
       ev_availability_prefix_name="EV_avail",
   )

Integration with EV Profiles
----------------------------

For standard (non-probabilistic) charging profiles, use
:func:`~flexgridpy.electrical_models.initializations.ev_conv_profiles.generate_conventional_ev_profiles`
which generates conventional charging and SoC trajectories.
