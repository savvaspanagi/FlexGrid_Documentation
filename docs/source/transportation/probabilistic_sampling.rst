Probabilistic Sampling
======================

Generate transportation data samples from truncated probability distributions.

Truncated Student-t Sample
--------------------------

.. autofunction:: flexgridpy.transportation_models.ev_probabilistic.truncated_t_samples.truncated_t_sample

Parameters
~~~~~~~~~~

**df** (*float*)
   Degrees of freedom of the Student-t distribution.

**loc** (*float*)
   Location parameter (mean center).

**scale** (*float*)
   Scale parameter (spread).

**a**, **b** (*float*)
   Lower and upper truncation bounds.

**size** (*int*)
   Number of samples to generate.

Returns
~~~~~~~

**numpy.ndarray**
   Array of sampled values within ``[a, b]``.

Example
-------

.. code-block:: python

   from flexgridpy.transportation_models.ev_probabilistic.truncated_t_samples import truncated_t_sample

   # Sample daily trip distances for 50 EVs
   trip_distances = truncated_t_sample(
       df=5,
       loc=30.0,    # mean around 30 km
       scale=10.0,  # spread
       a=5.0,       # minimum 5 km
       b=100.0,     # maximum 100 km
       size=50,
   )

   print(f"Mean distance: {trip_distances.mean():.1f} km")
   print(f"Min: {trip_distances.min():.1f}, Max: {trip_distances.max():.1f}")

Use Case
--------

This function is typically used to generate realistic distributions of EV trip
distances for Monte Carlo or stochastic optimization studies. The sampled
distances are converted to energy requirements and passed to the EV parameter
initialization functions in the electrical model.
