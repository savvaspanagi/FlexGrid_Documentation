addTime
=======



Function
--------

.. autofunction:: flexgridpy.electrical_models.variables.time_manager.addTime

Manager Method
--------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.addTime

Description
-----------

Sets the simulation **time horizon** and **time step** on the Manager. Must be
called before ``initialize_sets()`` so that ``STimes`` is correctly dimensioned.

Arguments
---------

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Argument
     - Description
   * - ``timeframe`` (float)
     - Total simulation horizon in **hours** (e.g. ``24`` for one day)
   * - ``time_interval`` (float)
     - Time step in **minutes** (e.g. ``60`` for hourly, ``15`` for 15-min)

Derived Quantities
------------------

.. math::

   |\mathcal{T}| = \frac{\text{timeframe} \times 60}{\text{time\_interval}}

.. math::

   \Delta t = \frac{\text{time\_interval}}{60} \quad \text{(hours)}

The value ``manager.delta`` is used in SoC and thermal dynamics constraints.



Example
-------

.. code-block:: python

   mgr.addTime(timeframe=24, time_interval=60)   # 24 hourly steps
   mgr.initialize_sets()                          # STimes = {0, 1, ..., 23}
