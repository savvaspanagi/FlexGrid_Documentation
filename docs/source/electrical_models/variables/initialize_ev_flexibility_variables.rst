initialize_ev_flexibility_variables
====================================

Description
-----------

Creates upward and downward **flexibility power** variables for each EV,
representing the available headroom for demand response.

Variables Created
-----------------

* ``pup_flex_ev[i, t]`` — upward flexibility power (p.u.)
* ``pdown_flex_ev[i, t]`` — downward flexibility power (p.u.)

Physical Meaning
--------------

* **Upward flexibility**: additional charging capacity the EV can offer to the grid
* **Downward flexibility**: reduction in charging the EV can provide

API Reference
-------------

.. autofunction:: flexgridpy.electrical_models.variables.def_ev_flex.initialize_ev_flexibility_variables

Manager Wrapper
---------------

.. automethod:: flexgridpy.electrical_models.Manager.Manager.initialize_ev_flexibility_variables

See Also
--------

* :doc:`../constraints_ev/add_power_up_flex_ev_cons`
* :doc:`../constraints_ev/add_power_down_flex_ev_cons`
