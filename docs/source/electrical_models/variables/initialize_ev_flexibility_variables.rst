initialize_ev_flexibility_variables
====================================

Function
--------

.. code-block:: python

   initialize_ev_flexibility_variables(manager, pup_flex_ev_name_prefix, pdown_flex_ev_name_prefix)

**Module:** ``flexgridpy.electrical_models.variables.def_ev_flex``

Manager Method
--------------

.. code-block:: python

   mgr.initialize_ev_flexibility_variables(...)

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


See Also
--------

* :doc:`../constraints_ev/add_power_up_flex_ev_cons`
* :doc:`../constraints_ev/add_power_down_flex_ev_cons`
